from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image2',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to='projects/',
                help_text="Second photo shown in the project's popup detail view (optional). Recommended: 800\u00d7500px or larger."
            ),
        ),
    ]
