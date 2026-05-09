from django.db import migrations


def update_projects(apps, schema_editor):
    Project = apps.get_model("portfolio", "Project")

    Project.objects.filter(slug="personal-document-brain").update(
        static_image="media/obsidian-brain.mp4",
        image_alt="Looping Obsidian second-brain graph video",
        featured=True,
        order=20,
    )

    Project.objects.filter(slug="google-ai-studio-media-project").update(
        static_image="media/google-ai-studio-video.mp4",
        image_alt="Looping Google AI Studio generated media video",
        order=40,
    )

    Project.objects.filter(slug="scikit-learn-predictive-model").update(
        static_image="",
        image_alt="scikit-learn model evaluation preview",
        order=50,
    )

    Project.objects.filter(slug="campus-skillswap").update(
        static_image="",
        image_alt="Campus SkillSwap app preview",
        github_link="https://github.com/sethco2/Project_Skills_Swap",
        demo_link="",
        featured=True,
        order=60,
    )

    Project.objects.filter(slug="conversational-chatbot").update(
        featured=False,
        order=95,
    )

    Project.objects.update_or_create(
        slug="learning-log",
        defaults={
            "title": "Learning Log",
            "category": "django",
            "featured": False,
            "order": 30,
            "static_image": "",
            "image_alt": "Learning Log Django app preview",
            "github_link": "https://github.com/sethco2/Project_LearningLog",
            "demo_link": "",
            "one_sentence_summary": (
                "A Django learning journal where users can create topics and keep entries "
                "tracking what they are learning over time."
            ),
            "business_problem": (
                "Learning new technical tools gets messy when notes are scattered across "
                "documents, screenshots, and half-finished files. Learning Log turns that "
                "process into a small web app where topics and entries stay organized, "
                "editable, and tied to a user account."
            ),
            "tools_used": (
                "Python, Django, SQLite, Django auth, Django forms, Django templates, "
                "HTML, CSS"
            ),
            "key_features": (
                "User accounts for private learning notes\n"
                "Create and manage learning topics\n"
                "Add dated entries under each topic\n"
                "Protected pages so users only see their own notes\n"
                "Django forms and templates for a clean CRUD workflow"
            ),
            "role_contribution": (
                "Built the Django app structure, models, forms, views, templates, routing, "
                "and authentication flow. This project helped me practice how Django pieces "
                "fit together in a real app instead of isolated exercises."
            ),
            "biggest_challenge": (
                "The hardest part was getting the user-specific data flow right. The app "
                "needed to make sure each topic and entry belonged to the logged-in user, "
                "which made authorization just as important as the form logic."
            ),
            "what_i_learned": (
                "Django makes more sense when you build the same feature all the way through: "
                "model, URL, view, form, template, and auth. Learning Log helped connect "
                "those pieces into one mental model."
            ),
        },
    )


class Migration(migrations.Migration):
    dependencies = [("portfolio", "0005_alter_project_category")]
    operations = [migrations.RunPython(update_projects, reverse_code=migrations.RunPython.noop)]
