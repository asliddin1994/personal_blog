from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.FileField(upload_to='post-images')
    tags = models.ManyToManyField("Tag", related_name='tags', blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    class Meta:
        app_label = 'postapp'
        ordering = ['-created_on']  # bu yangi qushilgan postni birinchi chiqaradi


    def __str__(self):  # bu metod tepadagi malumotlarni admin panelda string kurinishida chiqaradi
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
    parent = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='replies', blank=True, null=True)
    image = models.FileField(upload_to='comment-image', default='comment-image/user2.png')
    msg = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def getReplies(self):
        return Comment.objects.filter(parent=self).reverse()

    @property
    def isParent(self):
        if self.parent is None:
            return True
        return False
