# Generated by Django 4.2.2 on 2023-06-24 00:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("entries", "0003_remove_entry_post_date_entry_beer_style_entry_slug_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="entry",
            name="title",
        ),
        migrations.AddField(
            model_name="entry",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]