# Generated by Django 5.0.6 on 2024-05-24 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0007_alter_entry_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created',
        ),
    ]
