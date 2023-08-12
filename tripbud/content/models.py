from django.db import models
from PIL import Image
from django.contrib.auth.models import User
# Create your models here.

class newPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='post_pics')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
