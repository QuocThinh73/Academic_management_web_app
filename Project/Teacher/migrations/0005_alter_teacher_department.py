# Generated by Django 5.0.4 on 2024-04-29 19:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Databases", "0007_semester_semester_id"),
        ("Teacher", "0004_degrees_teacher_teaching_schedule_teacher_degrees"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teacher",
            name="department",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Databases.department",
            ),
        ),
    ]
