from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('client', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('completed', 'Completed'), ('ongoing', 'Ongoing')], max_length=20)),
                ('number', models.CharField(help_text='e.g., 01, 02, OG1, OG2', max_length=10)),
                ('badge_color', models.CharField(default='bg-blue-soft', help_text='CSS class for badge color (bg-blue-soft, bg-orange-soft, bg-green-soft, badge-purple)', max_length=50)),
                ('text_color', models.CharField(default='text-blue', help_text='CSS class for text color (text-blue, text-orange, text-green)', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Projects',
                'ordering': ['number'],
            },
        ),
    ]
