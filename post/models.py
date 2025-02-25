from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")


    def __str__(self):
        return self.title

class   Image(models.Model):  
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_images', null=True, blank=True)
    caption = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/") 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption

class   Document(models.Model):  
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_documents', null=True, blank=True)
    title = models.CharField(max_length=255)
    document = models.FileField(upload_to="documents/") 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
