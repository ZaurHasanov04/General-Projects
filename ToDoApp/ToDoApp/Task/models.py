from django.db import models

# Create your models here.

class Task(models.Model):
    text = models.TextField()
    creating_date= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.creating_date)
