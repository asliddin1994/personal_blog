from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=3)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
