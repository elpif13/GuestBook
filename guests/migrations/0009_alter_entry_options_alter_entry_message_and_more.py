# Generated by Django 5.0.6 on 2024-05-30 08:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("guests", "0008_remove_user_created"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="entry",
            options={
                "ordering": ["-created_entry"],
                "verbose_name": ("Entry",),
                "verbose_name_plural": ("Entries",),
            },
        ),
        migrations.AlterField(
            model_name="entry",
            name="message",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="entry",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="entry",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
