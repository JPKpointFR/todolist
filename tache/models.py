from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    creted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.description
