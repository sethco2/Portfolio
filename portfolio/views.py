import json

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import ContactForm
from .models import Experience, PersonalBuild, Project, Skill

# Extra media for specific projects (gallery, video, pdf).
# Stored here rather than in the DB to keep the schema simple.
_EXTRA_MEDIA = {
    "handyman-pricing-agent": {
        "type": "gallery",
        "images": [
            ("media/agent-orchestrator.png", "Agent Orchestrator — routes requests between agents"),
            ("media/agent-intake.png", "Intake Agent — classifies incoming customer requests"),
            ("media/agent-pricing.png", "Pricing Agent — generates structured quotes"),
            ("media/agent-scheduling.png", "Scheduling Agent — handles bookings"),
            ("media/agent-comms.png", "Comms Agent — drafts customer communications"),
        ],
    },
    "personal-document-brain": {
        "type": "video",
        "video": "media/obsidian-brain.mp4",
        "caption": "Obsidian second brain — graph view showing interconnected notes",
    },
    "google-ai-studio-media-project": {
        "type": "video_pdf",
        "video": "media/google-ai-studio-video.mp4",
        "pdf": "media/google-ai-studio-prompts.pdf",
        "pdf_label": "View Prompt Workflow PDF",
        "caption": "AI-generated media with consistent visual language",
    },
    "conversational-chatbot": {
        "type": "note",
        "note": (
            "This project is both the Chatbot Project and the LangChain Agent Project. "
            "The same codebase that powers the standalone chatbot scripts also drives the "
            "'Ask Seth' widget embedded on this site. Source in the Portfolio GitHub repo."
        ),
    },
}


def home(request):
    featured = Project.objects.filter(featured=True)[:3]
    if not featured.exists():
        featured = Project.objects.all()[:3]
    builds = PersonalBuild.objects.all()[:5]
    return render(request, "portfolio/home.html", {
        "featured_projects": featured,
        "personal_builds": builds,
    })


def about(request):
    return render(request, "portfolio/about.html")


def projects_index(request):
    projects = Project.objects.all()
    builds = PersonalBuild.objects.all()
    return render(request, "portfolio/projects_index.html", {
        "projects": projects,
        "personal_builds": builds,
    })


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    extra_media = _EXTRA_MEDIA.get(slug, {})
    return render(request, "portfolio/project_detail.html", {
        "project": project,
        "extra_media": extra_media,
    })


def skills(request):
    grouped = []
    for value, label in Skill.Group.choices:
        items = Skill.objects.filter(group=value)
        if items.exists():
            grouped.append((label, items))
    return render(request, "portfolio/skills.html", {"grouped": grouped})


def resume(request):
    experiences = Experience.objects.all()
    return render(request, "portfolio/resume.html", {"experiences": experiences})


_CHATBOT_SYSTEM_PROMPT = """
You are "Ask Seth" — a helpful assistant built into Seth Grant's portfolio website.
Your only job is to answer questions about Seth Grant, his projects, skills, background, and work.

About Seth:
- Baylor University, Hankamer School of Business, Honors College & Baylor Interdisciplinary Core
- BBA in MIS and Entrepreneurship & Corporate Innovation, May 2026, GPA 3.7
- Dean's Academic Honors List
- 22 years old, learning by building — applies AI to real problems
- He does NOT claim to be an expert in every tool; he explores and builds

Projects (class projects at Baylor):
1. HandyMan Pricing Agent — n8n multi-agent workflow (Intake, Pricing, Scheduling, Comms, Orchestrator agents) for service business automation
2. Conversational Chatbot / LangChain Agent — LangChain + Google Gemini chatbot; this IS both the chatbot project and the LangChain project
3. Google AI Studio Media Project — AI media generation using Google AI Studio and Gemini; includes prompt workflow PDF
4. scikit-learn Predictive Model — three ML scripts (iris.py, diabetes.py, ml1.py) using KNN and linear regression
5. Campus SkillSwap — full Django CRUD web app for student skill exchange; GitHub: https://github.com/sethco2/Project_Skills_Swap
6. Personal Document Brain — Obsidian-based second brain system connecting notes, research, and projects

Personal ventures:
- AuraAnn Skincare (auraannskincare.com) — skincare brand, AI-driven content and brand strategy
- MineralsRx (mineralsrx.com) — wellness supplement brand
- LymeRevive.org — nonprofit education platform organizing Lyme disease information

Work experience: Lakeway Marina, Virtual Force, Eve Vehicles
Leadership: Tau Kappa Epsilon Histor, Baylor Honors College, Church Under the Bridge volunteer
Top 50 Baylor New Venture Competition

Skills: AI prompting, LangChain agents, n8n workflows, Claude API, Google Gemini, Google AI Studio, Django, Python, HTML/CSS, JavaScript, scikit-learn, pandas, Shopify API, brand strategy

Contact: sethngrant2003@gmail.com | LinkedIn: https://www.linkedin.com/in/sethngrant/ | GitHub: https://github.com/sethco2

Rules:
- ONLY answer questions about Seth Grant, his portfolio, projects, skills, background, contact info, and work
- If asked anything unrelated (general coding help, weather, politics, etc.), respond:
  "I'm built to answer questions about Seth Grant, his portfolio, projects, skills, and background. Is there something specific about Seth's work you'd like to know?"
- Be friendly, concise, and honest — Seth is still learning and that's fine
- Do not make up information not listed above
- Keep answers brief (2-4 sentences unless more detail is clearly needed)
""".strip()


@require_POST
@csrf_exempt
def chatbot(request):
    api_key = getattr(settings, "GEMINI_API_KEY", "")
    if not api_key:
        return JsonResponse(
            {"reply": "The Ask Seth chatbot isn't connected yet — GEMINI_API_KEY is not configured. In the meantime, feel free to browse the projects or reach out via the Contact page."},
            status=200,
        )

    try:
        data = json.loads(request.body)
        user_message = (data.get("message") or "").strip()[:1000]
        if not user_message:
            return JsonResponse({"reply": "I didn't catch that — try typing your question."}, status=200)

        from google import genai
        from google.genai import types
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=user_message,
            config=types.GenerateContentConfig(
                system_instruction=_CHATBOT_SYSTEM_PROMPT,
                temperature=0.4,
                max_output_tokens=400,
            ),
        )
        reply = response.text.strip()
        return JsonResponse({"reply": reply})

    except Exception:
        return JsonResponse(
            {"reply": "Something went wrong on my end. Try the Contact page to reach Seth directly."},
            status=200,
        )


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        # Honeypot — silently drop bot submissions.
        if form.cleaned_data.get("website"):
            return redirect("portfolio:contact")

        contact_to = getattr(settings, "CONTACT_EMAIL", "")
        try:
            if contact_to:
                send_mail(
                    subject=f"[Portfolio] {form.cleaned_data.get('subject') or 'New message'}",
                    message=(
                        f"From: {form.cleaned_data['name']} <{form.cleaned_data['email']}>\n\n"
                        f"{form.cleaned_data['message']}"
                    ),
                    from_email=getattr(settings, "DEFAULT_FROM_EMAIL", contact_to),
                    recipient_list=[contact_to],
                    fail_silently=False,
                )
                messages.success(request, "Thanks — your message was sent.")
            else:
                messages.info(
                    request,
                    "SMTP isn't configured yet. Use the email link below or "
                    "add EMAIL_* env vars to enable the form.",
                )
        except Exception:
            messages.warning(
                request,
                "Couldn't send right now. Please email me directly using the link below.",
            )
        return redirect("portfolio:contact")

    return render(request, "portfolio/contact.html", {"form": form})
