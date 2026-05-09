from django.db import migrations


def update_video_media(apps, schema_editor):
    Project = apps.get_model("portfolio", "Project")
    Project.objects.filter(slug="campus-skillswap").update(
        static_image="media/campus-skillswap-demo.mp4",
        image_alt="Looping Campus SkillSwap app walkthrough video",
    )
    Project.objects.filter(slug="learning-log").update(
        static_image="media/learning-log-demo.mp4",
        image_alt="Looping Learning Log app walkthrough video",
    )


class Migration(migrations.Migration):
    dependencies = [("portfolio", "0006_learning_log_and_media_previews")]
    operations = [migrations.RunPython(update_video_media, reverse_code=migrations.RunPython.noop)]
