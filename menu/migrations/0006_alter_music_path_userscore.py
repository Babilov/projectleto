# Generated by Django 4.1.1 on 2022-09-20 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("menu", "0005_music_file_alter_music_name_alter_music_path"),
    ]

    operations = [
        migrations.AlterField(
            model_name="music",
            name="path",
            field=models.CharField(max_length=300),
        ),
        migrations.CreateModel(
            name="UserScore",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("score", models.IntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
