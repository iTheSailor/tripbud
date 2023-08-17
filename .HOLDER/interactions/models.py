# from django.db import models
# from django.db.models.fields.related import ForeignKey
# from django.contrib.auth.models import User
# from django.utils import timezone

# # Create your models here.

# class FriendsList(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
#     friends = models.ManyToManyField(User, blank=True, related_name="friends")

#     def __str__(self):
#         return self.user.username
    
#     def add_friend(self, account):
#         if not account in self.friends.all():
#             self.friends.add(account)
#             self.save()