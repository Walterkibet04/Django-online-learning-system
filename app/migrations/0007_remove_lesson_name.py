# Generated by Django 4.2.7 on 2024-05-05 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_lesson_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='name',
        ),
    ]