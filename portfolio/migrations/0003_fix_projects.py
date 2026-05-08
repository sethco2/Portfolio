"""
Fix project categories, images, and personal build URLs.
- HandyMan: category langchain -> n8n, images -> agent screenshots
- Conversational Chatbot: category chatbot -> langchain (it IS the LangChain project)
- Personal Document Brain: category n8n -> other, note Obsidian video
- Update LymeRevive URL to lymerevive.org
- Update github_link for all class projects -> sethco2
- Update scikit-learn project details based on actual files
"""
from django.db import migrations


def fix_data(apps, schema_editor):
    Project = apps.get_model("portfolio", "Project")
    PersonalBuild = apps.get_model("portfolio", "PersonalBuild")

    # --- HandyMan Pricing Agent: fix category + images ---
    try:
        p = Project.objects.get(slug="handyman-pricing-agent")
        p.category = "n8n"
        p.static_image = "media/agent-orchestrator.png"
        p.image_alt = "HandyMan Agent Orchestrator workflow"
        p.github_link = "https://github.com/sethco2"
        p.one_sentence_summary = (
            "An AI agent workflow for a handyman-style service business that routes "
            "customer intake, pricing, scheduling, and communication through connected agents."
        )
        p.business_problem = (
            "Service businesses lose significant time manually handling customer requests, "
            "quoting jobs, scheduling appointments, and following up on communications. "
            "Every one of those steps is a manual handoff that creates delays and mistakes. "
            "This workflow shows how AI agents can connect those steps into a system that "
            "routes each type of request to the right agent automatically."
        )
        p.tools_used = (
            "n8n, AI agent orchestration, Intake Agent, Pricing Agent, Scheduling Agent, "
            "Comms Agent, workflow automation, JSON, dotenv"
        )
        p.key_features = (
            "Intake Agent collects and classifies incoming customer requests\n"
            "Pricing Agent generates structured quote estimates\n"
            "Scheduling Agent handles appointment availability and booking\n"
            "Comms Agent drafts and routes customer communications\n"
            "Orchestrator workflow routes requests between agents based on intent\n"
            "Secrets isolated in .env so the workflow is safe to share"
        )
        p.role_contribution = (
            "I designed the full multi-agent system: the orchestrator logic, each agent's "
            "role and scope, the data flow between agents, and the output format each one "
            "produces. Built to show how a single customer interaction can touch multiple "
            "automated agents without any manual handoffs."
        )
        p.biggest_challenge = (
            "Getting the orchestrator to route correctly without agents stepping on each "
            "other. The fix was giving each agent a strict input schema and output contract, "
            "so the orchestrator always knew what format to expect and where to route next."
        )
        p.what_i_learned = (
            "Multi-agent systems are mostly coordination problems. Each individual agent is "
            "simple. The real design work is in the handoffs between them — what data passes, "
            "in what format, and what happens when something is ambiguous."
        )
        p.save()
    except Project.DoesNotExist:
        pass

    # --- Conversational Chatbot: fix category to langchain ---
    try:
        p = Project.objects.get(slug="conversational-chatbot")
        p.category = "langchain"
        p.github_link = "https://github.com/sethco2/Portfolio"
        p.one_sentence_summary = (
            "A LangChain-powered conversational agent built with Google Gemini — "
            "this is both the chatbot project and the LangChain agent project."
        )
        p.business_problem = (
            "Most chatbots either over-promise or wander off topic. The goal here was to "
            "build something disciplined using LangChain's agent framework: a small assistant "
            "with a clear scope that stays useful instead of becoming generic. "
            "The same codebase powers the 'Ask Seth' widget on this site."
        )
        p.tools_used = (
            "Python, LangChain, Google Gemini (gemini-2.5-flash), dotenv, "
            "create_agent, system prompt engineering"
        )
        p.key_features = (
            "Built with LangChain's create_agent framework using Google Gemini\n"
            "Tightly scoped system prompt that defines tone and boundaries\n"
            "Conversation memory through message history\n"
            "Two versions: interactive loop (v1) and single-prompt demo (v2)\n"
            "Foundation for the Ask Seth chatbot widget embedded on this site\n"
            "Falls back gracefully when asked something outside its scope"
        )
        p.role_contribution = (
            "Wrote both chatbot versions from prompt design outward, iterating until the "
            "agent felt direct, polite, and useful within its defined scope. "
            "Extended the same architecture into the portfolio's Ask Seth widget."
        )
        p.biggest_challenge = (
            "Keeping personality and clarity in the same prompt. Too much personality and "
            "the bot wanders off topic; too much rigidity and it feels like a form. "
            "The balance came from short, sharp rules in the system message."
        )
        p.what_i_learned = (
            "The interface is the prompt. Most of what users feel about a chatbot is decided "
            "in the first paragraph of the system message. LangChain's agent abstraction makes "
            "it easy to swap models and tools without rewriting the logic."
        )
        p.save()
    except Project.DoesNotExist:
        pass

    # --- Personal Document Brain: fix category to personal ---
    try:
        p = Project.objects.get(slug="personal-document-brain")
        p.category = "personal"
        p.static_image = "media/n8n-workflow.png"
        p.image_alt = "Obsidian knowledge graph second brain"
        p.github_link = ""
        p.one_sentence_summary = (
            "A personal knowledge system built around Obsidian that turns scattered notes, "
            "research, projects, and ideas into an interconnected second brain."
        )
        p.business_problem = (
            "AI tools are powerful but they forget context constantly. People collect "
            "information in scattered folders, apps, and notes that never connect to each "
            "other. This system solves that by building an interconnected knowledge graph "
            "that links everything I learn, research, build, and save — so ideas connect "
            "instead of disappearing."
        )
        p.tools_used = (
            "Obsidian, markdown, knowledge graph, n8n, AI research workflows, "
            "Claude API, Google Drive, automation"
        )
        p.key_features = (
            "Interconnected Obsidian vault with graph view linking notes across topics\n"
            "Ingests research, project notes, and saved content from multiple sources\n"
            "AI-assisted tagging and cross-linking so connections surface automatically\n"
            "Manages information over time — the system maintains itself\n"
            "Solves the problem of AI and people forgetting context\n"
            "Supports learning by connecting ideas instead of filing them in folders"
        )
        p.role_contribution = (
            "Designed and built the full system: the Obsidian vault structure, the note "
            "templates, the tagging convention, and the automation workflow that keeps it "
            "current. This is an ongoing personal tool, not a one-time class project."
        )
        p.biggest_challenge = (
            "Keeping the system from drifting into noise. Every knowledge system eventually "
            "becomes a junk drawer unless you design strict templates for what goes in and "
            "how it connects. The fix was writing the rules before writing any notes."
        )
        p.what_i_learned = (
            "A second brain is not a bigger notebook. The value is in the edges between notes, "
            "not the notes themselves. Designing for connection first changes how you build "
            "the whole system."
        )
        p.save()
    except Project.DoesNotExist:
        pass

    # --- Google AI Studio: update github link ---
    try:
        p = Project.objects.get(slug="google-ai-studio-media-project")
        p.github_link = ""
        p.static_image = "media/google-ai-studio-media.png"
        p.image_alt = "Google AI Studio media generation project"
        p.save()
    except Project.DoesNotExist:
        pass

    # --- scikit-learn: update with real file details ---
    try:
        p = Project.objects.get(slug="scikit-learn-predictive-model")
        p.github_link = "https://github.com/sethco2/Portfolio"
        p.one_sentence_summary = (
            "Three supervised machine learning scripts using Python and scikit-learn "
            "to classify and predict across the Iris, Diabetes, and Digits datasets."
        )
        p.business_problem = (
            "Most business decisions hinge on some kind of prediction or classification. "
            "These three scripts build the core ML muscle: loading real datasets, training "
            "models, evaluating performance honestly, and visualizing what the model got "
            "right and wrong. The goal was to understand the full pipeline before touching "
            "more complex problems."
        )
        p.tools_used = (
            "Python, scikit-learn, KNeighborsClassifier, LinearRegression, "
            "train_test_split, confusion_matrix, pandas, NumPy, seaborn, matplotlib"
        )
        p.key_features = (
            "iris.py — KNN classification on Iris flower dataset (150 samples, 4 features), "
            "confusion matrix heatmap, accuracy score\n"
            "diabetes.py — Linear regression on Diabetes dataset using blood glucose (s6) "
            "feature, scatterplot with regression line\n"
            "ml1.py — KNN on Digits dataset (1797 handwritten digit images), "
            "confusion matrix, accuracy score\n"
            "All three use proper train/test splits with random_state for reproducibility\n"
            "Visualizations generated with seaborn and matplotlib"
        )
        p.role_contribution = (
            "Wrote all three scripts from scratch: load, explore, split, train, predict, "
            "evaluate, and visualize. Compared the KNN and LinearRegression approaches on "
            "different data types to see where each model earns its keep."
        )
        p.biggest_challenge = (
            "Understanding that a high accuracy score is not the whole story. The confusion "
            "matrix shows you exactly where the model is wrong and on which classes. "
            "Learning to read that before celebrating the accuracy number was the real lesson."
        )
        p.what_i_learned = (
            "ML feels like coding but acts like science. The discipline is in the questions "
            "you ask of the data before you fit anything. Visualizing the confusion matrix "
            "taught me more than the accuracy score did."
        )
        p.save()
    except Project.DoesNotExist:
        pass

    # --- Campus SkillSwap: fix github link ---
    try:
        p = Project.objects.get(slug="campus-skillswap")
        p.github_link = "https://github.com/sethco2/Project_Skills_Swap"
        p.demo_link = ""
        p.save()
    except Project.DoesNotExist:
        pass

    # --- Fix LymeRevive URL in PersonalBuilds ---
    try:
        b = PersonalBuild.objects.get(name="LymeReviveFoundation.org")
        b.name = "LymeRevive.org"
        b.url = "https://lymerevive.org"
        b.summary = (
            "A nonprofit education platform I am building to organize complex Lyme "
            "disease information into a clearer public resource."
        )
        b.save()
    except PersonalBuild.DoesNotExist:
        pass

    # --- Add Personal Document Brain to personal builds if not present ---
    PersonalBuild.objects.update_or_create(
        name="Personal Document Brain",
        defaults={
            "summary": (
                "An Obsidian-based second brain that connects research, notes, "
                "projects, and lessons learned into an interconnected knowledge system."
            ),
            "url": "",
            "order": 55,
        },
    )


def reverse_fix(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [("portfolio", "0002_seed_content")]
    operations = [migrations.RunPython(fix_data, reverse_code=reverse_fix)]
