# Generated by Django 5.0.4 on 2024-04-18 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0005_remove_myuser_is_student_remove_myuser_is_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentuser',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='teacheruser',
            name='teacher_id',
        ),
    ]
