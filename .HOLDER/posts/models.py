from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from maps import Map
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    post_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=500, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tagged_map = models.ForeignKey(Map, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='post_pics', blank=True, default='post_pics/default.png')
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    comments = models.ManyToManyField(User, related_name='comments', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def get_post_by_id(self,post_id):
        post = post_id
        return post
    
    def get_all_posts_by_author(self,author):
        posts = Post.objects.filter(author=author)
        return posts
    
    def delete_post(self,post_id):
        post = post_id
        post.delete()
        return post
    
    def edit_post(self,post_id,data):
        post = post_id
        for key, value in data.items():
            setattr(post, key, value)
        post.save()
        return post
    
    def add_map(self,post_id, map_id):
        post = post_id
        _map = map_id
        post.tagged_map = _map
        post.save()
        return post
    
    def remove_map(self,post_id):
        post = post_id
        post.tagged_map = None
        post.save()
        return post