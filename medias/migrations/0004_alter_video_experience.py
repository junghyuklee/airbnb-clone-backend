# Generated by Django 4.2.1 on 2023-07-12 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0005_alter_experience_perks'),
        ('medias', '0003_alter_photo_file_alter_video_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='experience',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='video', to='experiences.experience'),
        ),
    ]
