# Generated by Django 5.0.6 on 2024-05-24 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0005_alter_entry_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-created'], 'verbose_name': 'Entry', 'verbose_name_plural': 'Entries'},
        ),
    ]
