# Generated by Django 4.0.4 on 2022-10-18 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='course',
            new_name='courses',
        ),
    ]