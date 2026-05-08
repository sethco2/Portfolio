"""Set Personal Document Brain category to 'personal'."""
from django.db import migrations


def fix_category(apps, schema_editor):
    Project = apps.get_model("portfolio", "Project")
    Project.objects.filter(slug="personal-document-brain").update(category="personal")


class Migration(migrations.Migration):
    dependencies = [("portfolio", "0003_fix_projects")]
    operations = [migrations.RunPython(fix_category, reverse_code=migrations.RunPython.noop)]
