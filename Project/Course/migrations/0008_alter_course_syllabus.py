# Generated by Django 5.0.4 on 2024-05-02 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0007_course_description_course_syllabus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='syllabus',
            field=models.TextField(null=True),
        ),
    ]
