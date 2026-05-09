from django.db import migrations


PROJECT_COPY = {
    "handyman-pricing-agent": {
        "one_sentence_summary": (
            "A multi-agent handyman workflow that was cool to build, frustrating to get "
            "working, and most useful as a lesson in how AI can coordinate messy business steps."
        ),
        "business_problem": (
            "The idea was simple: a handyman-style business has to deal with intake, pricing, "
            "scheduling, and customer communication, and those steps can get messy fast. I wanted "
            "to see if AI agents could help connect those pieces into one workflow. It was not as "
            "smooth as it sounds. A lot of the project was figuring out how to make the agents "
            "stop overcomplicating things and actually pass useful information from one step to "
            "the next."
        ),
        "key_features": (
            "Intake Agent for understanding what the customer is asking for\n"
            "Pricing Agent for turning the request into a rough quote structure\n"
            "Scheduling Agent for thinking through availability and booking steps\n"
            "Comms Agent for drafting customer-facing messages\n"
            "Orchestrator workflow that connects the agents instead of treating them like isolated bots\n"
            "Cleaner prompting and connector setup after the first versions got too fragile"
        ),
        "role_contribution": (
            "I worked through the agent setup, the roles for each step, and the orchestration "
            "logic. The biggest shift was realizing that trying to manually control every little "
            "connector was making the project harder. Letting AI help handle the connector logic, "
            "while giving it very clear prompts and boundaries, worked better than trying to force "
            "everything by hand."
        ),
        "biggest_challenge": (
            "This project was honestly frustrating. The pieces made sense separately, but getting "
            "them to work together was the hard part. The agents could misunderstand each other, "
            "the workflow could break in small ways, and it took a lot of iteration to make the "
            "handoffs feel reliable."
        ),
        "what_i_learned": (
            "I learned that agent workflows are less about making one smart bot and more about "
            "designing clean handoffs. The prompting mattered more than I expected. Once the agents "
            "had clearer jobs and the connector work was handled more naturally, the system made a "
            "lot more sense. It also showed me why businesses could care about this: not because it "
            "is flashy, but because intake, quoting, scheduling, and communication are real time sinks."
        ),
    },
    "personal-document-brain": {
        "one_sentence_summary": (
            "A personal Obsidian-based knowledge system built because I needed one place where AI "
            "could help me work with my notes instead of constantly forgetting the context."
        ),
        "business_problem": (
            "The problem came from my own workflow. I save notes, research, project ideas, class "
            "material, and business thoughts in a lot of different places. Then when I use AI, it "
            "does not remember all of that context unless I bring it back every time. The Personal "
            "Document Brain is my attempt to make one connected place where that information can "
            "live, so AI and I can both work from the same base of knowledge."
        ),
        "key_features": (
            "Obsidian vault organized around connected notes instead of random folders\n"
            "Graph view that shows how different notes, projects, and ideas relate\n"
            "A single place to collect research, class material, business ideas, and project notes\n"
            "Designed to make it easier to bring context back into AI conversations\n"
            "Built around the way I actually learn: saving, connecting, revisiting, and building from notes"
        ),
        "role_contribution": (
            "I built the structure around how I actually think and work. This was not meant to be "
            "a perfect productivity system. It was a way to make my notes useful again, especially "
            "when I am using AI and need to quickly reconnect it to what I have already learned or saved."
        ),
        "biggest_challenge": (
            "The challenge is keeping it useful instead of letting it become another place where "
            "information goes to die. A knowledge system only helps if the notes connect and stay "
            "easy to return to. Otherwise it is just a nicer-looking folder."
        ),
        "what_i_learned": (
            "I learned that the real value is not just storing notes. It is being able to return to "
            "them with context. This project made me think more seriously about how AI tools could "
            "be better if they had access to the right long-term knowledge instead of starting fresh "
            "every conversation."
        ),
    },
    "scikit-learn-predictive-model": {
        "one_sentence_summary": (
            "A set of scikit-learn exercises that made machine learning feel less abstract and made "
            "me curious about where prediction models could actually be useful."
        ),
        "business_problem": (
            "This was a class-style machine learning project, so it was not solving one specific "
            "business problem yet. But it made the bigger idea click: a lot of decisions come down "
            "to classification or prediction. Whether it is identifying patterns, forecasting outcomes, "
            "or sorting data into useful categories, the structure behind these small examples has "
            "real business potential."
        ),
        "key_features": (
            "Iris classification using KNN to predict flower species from measurements\n"
            "Digits classification using KNN to recognize handwritten numbers\n"
            "Diabetes regression using one feature to explore prediction with a regression line\n"
            "Train/test splits so the model is evaluated on data it did not train on\n"
            "Confusion matrices and charts to see what the model got right and wrong"
        ),
        "role_contribution": (
            "I wrote and ran the scripts, worked through the datasets, and used the visual outputs "
            "to understand what the models were actually doing. The interesting part was not just "
            "getting a score. It was seeing how a model turns data into a prediction and then checking "
            "where that prediction fails."
        ),
        "biggest_challenge": (
            "The hardest part was understanding what the results really meant. It is easy to see an "
            "accuracy score and move on, but the confusion matrix and regression plot made me slow "
            "down and ask better questions about what the model was learning."
        ),
        "what_i_learned": (
            "This project was really interesting because it made me wonder about practical use cases. "
            "The examples were small, but the pattern is big: if you can structure the data, you can "
            "start asking prediction questions. I am still learning the deeper math and tradeoffs, "
            "but I can see why scikit-learn is useful for exploring ideas before building something larger."
        ),
    },
    "campus-skillswap": {
        "one_sentence_summary": (
            "A fun Django project for trading skills on campus, with a frontend theme that came "
            "together much better once I used AI to help shape the design."
        ),
        "business_problem": (
            "The idea was straightforward: students know useful things, but it is not always easy "
            "to find the person who can help with a specific skill. SkillSwap turns that into a small "
            "campus marketplace where people can post what they know and browse what others are offering. "
            "It was a fun class project, and the most satisfying part was seeing the app start to feel "
            "like something people could actually click around in."
        ),
        "key_features": (
            "Student skill listings with create, edit, and delete flows\n"
            "Browse page for seeing what other students are offering\n"
            "User accounts so people can manage their own listings\n"
            "Django models, views, forms, templates, and URL routing\n"
            "Frontend theme implemented with help from an AI frontend design workflow"
        ),
        "role_contribution": (
            "I built the Django structure and worked through the app flow, then used the frontend "
            "design skill to improve the look and feel. That part honestly did a fantastic job. It "
            "helped turn the project from a plain Django assignment into something with a real theme "
            "and personality."
        ),
        "biggest_challenge": (
            "The hard part was getting the app to feel like one connected experience instead of a "
            "collection of CRUD pages. Django gives you the pieces, but the design and navigation are "
            "what make it feel usable."
        ),
        "what_i_learned": (
            "I learned that frontend presentation changes how a project feels, even when the backend "
            "logic is simple. SkillSwap was a good reminder that an app can be technically correct and "
            "still feel unfinished until the interface has a clear theme and flow."
        ),
    },
    "learning-log": {
        "one_sentence_summary": (
            "A simple Django learning journal that helped me understand the basic rhythm of building "
            "models, views, forms, templates, and user-specific pages."
        ),
        "business_problem": (
            "Learning Log is not trying to be a major product. It is a practice app, and that is okay. "
            "The point was to build something small enough to understand but complete enough to show "
            "how Django apps work: users, topics, entries, forms, and protected pages."
        ),
        "key_features": (
            "User accounts for keeping learning notes private\n"
            "Topics that organize what someone is learning\n"
            "Entries under each topic for saving progress over time\n"
            "Create and edit flows built with Django forms\n"
            "A clean walkthrough video showing the app in use"
        ),
        "role_contribution": (
            "I used this project to practice the core Django pattern from end to end. It helped me "
            "see how a model connects to a form, how a view sends data to a template, and how the URL "
            "structure holds the whole thing together."
        ),
        "biggest_challenge": (
            "The challenge was not one huge technical problem. It was keeping all the Django pieces "
            "straight at the same time. Once the pattern clicked, the app started to feel much less mysterious."
        ),
        "what_i_learned": (
            "I learned that small projects are useful because they make the structure visible. Learning "
            "Log gave me a cleaner mental model for Django, which made later projects like SkillSwap feel "
            "more approachable."
        ),
    },
}


def update_reflections(apps, schema_editor):
    Project = apps.get_model("portfolio", "Project")
    for slug, fields in PROJECT_COPY.items():
        Project.objects.filter(slug=slug).update(**fields)


class Migration(migrations.Migration):
    dependencies = [("portfolio", "0008_update_google_ai_studio_copy")]
    operations = [migrations.RunPython(update_reflections, reverse_code=migrations.RunPython.noop)]
