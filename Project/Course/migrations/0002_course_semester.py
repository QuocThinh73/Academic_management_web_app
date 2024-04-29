# Generated by Django 5.0.4 on 2024-04-29 19:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Course", "0001_initial"),
        ("Databases", "0007_semester_semester_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="semester",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Databases.semester",
            ),
        ),
    ]
