from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to='projects/',
                help_text='Photo shown on the project card (optional). Recommended: 800\u00d7500px or larger.'
            ),
        ),
    ]
