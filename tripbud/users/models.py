from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
from .managers import CustomUserManager
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=256, unique=True)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=256)
    bio = models.TextField(max_length=500, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    friends = models.ManyToManyField("self", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    
    objects = CustomUserManager()


# class Profile(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     profile_pic = models.ImageField(upload_to='profile_pics', blank=True, default='profile_pics/default.png')
#     friends = models.ManyToManyField(CustomUser, blank=True, related_name='friends')
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"{self.user.username}-{self.created.strftime('%d-%m-%Y')}"
    
#     def get_friends(self):
#         return self.friends.all()
    
#     def get_friends_no(self):
#         return self.friends.all().count()
    
#     def get_posts_no(self):
#         return self.posts.all().count()
    
#     def get_all_authors_posts(self):
#         return self.posts.all()
    
#     def get_likes_given_no(self):
#         likes = self.like_set.all()
#         total_liked = 0
#         for item in likes:
#             if item.value == 'Like':
#                 total_liked += 1
#         return total_liked
    
#     def get_likes_recieved_no(self):
#         posts = self.posts.all()
#         total_liked = 0
#         for item in posts:
#             total_liked += item.liked.all().count()
#         return total_liked
    
#     def get_posts_no(self):
#         return self.posts.all().count()
    
#     def get_all_authors_posts(self):
#         return self.posts.all().order_by('-created')
    
#     def get_likes_given_no(self):
#         likes = self.like_set.all()
#         total_liked = 0
#         for item in likes:
#             if item.value == 'Like':
#                 total_liked += 1
#         return total_liked
    
#     def get_likes_recieved_no(self):
#         posts = self.posts.all()
#         total_liked = 0
#         for item in posts:
#             total_liked += item.liked.all().count()
#         return total_liked
    
#     def get_posts_no(self):
#         return self.posts.all().count()
    
#     def get_all_authors_posts(self):
#         return self.posts.all().order_by('-created')
    
#     def get_likes_given_no(self):
#         likes = self.like_set.all()
#         total_liked = 0
#         for item in likes:
#             if item.value == 'Like':
#                 total_liked += 1
#         return
    