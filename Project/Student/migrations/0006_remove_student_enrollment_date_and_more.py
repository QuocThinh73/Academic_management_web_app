# Generated by Django 5.0.4 on 2024-04-24 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Databases", "0002_department_major"),
        ("Student", "0005_student_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="enrollment_date",
        ),
        migrations.AlterField(
            model_name="student",
            name="department",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Databases.department",
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="major",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Databases.major",
            ),
        ),
    ]
