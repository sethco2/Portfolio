from django.db import migrations


def update_copy(apps, schema_editor):
    Project = apps.get_model("portfolio", "Project")
    Project.objects.filter(slug="google-ai-studio-media-project").update(
        one_sentence_summary=(
            "A class media-generation experiment using Google AI Studio to learn how "
            "prompting, iteration, and visual planning affect AI-generated video."
        ),
        business_problem=(
            "This project was less about producing a finished brand asset and more about "
            "understanding the early workflow. The video itself is rough and has some of "
            "the obvious AI weirdness people notice right away, but that is part of what "
            "made it useful. It showed how fast the tools are improving, how much prompt "
            "structure matters, and where AI-generated media could eventually help small "
            "businesses create drafts, concepts, ads, product visuals, or campaign ideas "
            "more quickly."
        ),
        tools_used=(
            "Google AI Studio, Gemini, AI video generation, prompt engineering, "
            "visual planning, iteration, PDF workflow notes"
        ),
        key_features=(
            "Generated a short experimental AI video from class prompts\n"
            "Used an annotated PDF to document the prompt and visual planning workflow\n"
            "Compared the intended concept against the rough generated output\n"
            "Practiced iteration instead of treating the first output as final\n"
            "Identified realistic business uses for future AI media workflows"
        ),
        role_contribution=(
            "I worked through the prompt and media-generation process, reviewed what the "
            "model produced, and connected the exercise back to practical business use "
            "cases. The goal was not to present the video as polished work. It was to learn "
            "the basics of Google AI Studio and understand what would need to improve before "
            "using this type of workflow for real brand or product content."
        ),
        biggest_challenge=(
            "The biggest challenge was that the output still looked like obvious AI slop in "
            "places. Instead of pretending it was polished, the useful part was noticing why "
            "it failed: weak visual consistency, odd motion, and moments where the model did "
            "not fully understand the intended scene. That made the project a better learning "
            "exercise."
        ),
        what_i_learned=(
            "I learned that AI media generation is powerful, but it still needs direction, "
            "taste, and editing. The roughness of the video made the lesson clearer: these "
            "tools are not magic finished-output machines yet, but they are already useful "
            "for exploring ideas quickly. I can see real business potential in better prompt "
            "workflows, especially for concepts, early creative drafts, and content planning."
        ),
    )


class Migration(migrations.Migration):
    dependencies = [("portfolio", "0007_skillswap_learning_log_videos")]
    operations = [migrations.RunPython(update_copy, reverse_code=migrations.RunPython.noop)]
