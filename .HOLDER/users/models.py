from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # following = models.ManyToManyField(User, related_name='following', blank=True)
    # followers = models.ManyToManyField(User, related_name='followers', blank=True)
    # friends = models.ManyToManyField(User, related_name='friends', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    # profile_pic = models.ImageField(upload_to='profile_pics', blank=True, default='profile_pics/default.png')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}"
    
    # def profile_posts(self):
    #     return self.posts.all().order_by('-created_at')
    
    # def get_posts(self):
    #     return self.posts.all()
    
    # def get_posts_count(self):
    #     return self.posts.all().count()
    
    # def get_friends(self):
    #     return self.friends.all()
    
    # def friends_count(self):
    #     return self.friends.all().count()
    
    # def get_following(self):
    #     return self.following.all()
    
    # def following_count(self):
    #     return self.following.all().count()
    
    # def get_followers(self):
    #     return self.followers.all()
    
    # def followers_count(self):
    #     return self.followers.all().count()
    

STATUS_CHOICES = (
    ('send', 'send'),
    ('accepted', 'accepted'),
)

class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"
    
