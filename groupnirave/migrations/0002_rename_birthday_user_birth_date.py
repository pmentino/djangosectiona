# Generated by Django 5.0.6 on 2024-05-25 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groupnirave', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='birthday',
            new_name='birth_date',
        ),
    ]