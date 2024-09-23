from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'contactapp'
        ordering = ['-created_on']
    def __str__(self):
        return self.name
