# Generated by Django 5.0.4 on 2024-04-20 04:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Student", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="studentuser",
            name="student_id",
        ),
        migrations.AddField(
            model_name="studentuser",
            name="department",
            field=models.CharField(default="", max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="studentuser",
            name="name",
            field=models.CharField(default="", max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="studentuser",
            name="date_of_birth",
            field=models.DateField(default="", null=True),
        ),
        migrations.AlterField(
            model_name="studentuser",
            name="enrollment_date",
            field=models.DateField(default="", null=True),
        ),
        migrations.AlterField(
            model_name="studentuser",
            name="id",
            field=models.CharField(
                default="", max_length=15, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="studentuser",
            name="major",
            field=models.CharField(default="", max_length=50, null=True),
        ),
    ]
