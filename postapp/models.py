from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.FileField(upload_to='post-images')
    tags = models.ManyToManyField("Tag", related_name='tags', blank=True)
    is_approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)  # Ko'rishlar soni
    recommended = models.BooleanField(default=False)  # Tavsiya qilingan

    class Meta:
        app_label = 'postapp'
        ordering = ['-created_on']

    def __str__(self):
        return str(self.title)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    website = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', blank=True, null=True)
    image = models.FileField(upload_to='comment-image', default='comment-image/jack.jpg')
    msg = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def get_replies(self):
        return Comment.objects.filter(parent=self).order_by('-created_on')

    @property
    def is_parent(self):
        return self.parent is None
