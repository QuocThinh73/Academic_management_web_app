from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=50, null=True, default="")
    credit = models.IntegerField(default=0)

    def __str__(self):
        return self.name
