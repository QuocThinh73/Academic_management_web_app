# Generated by Django 5.0.4 on 2024-04-29 19:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Databases", "0005_alter_semester_semester_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="semester",
            name="semester_id",
        ),
    ]
