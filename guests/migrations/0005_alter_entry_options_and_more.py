# Generated by Django 5.0.6 on 2024-05-24 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0004_alter_entry_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='created_date_entry',
            new_name='created',
        ),
    ]
