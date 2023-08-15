from django.contrib.auth.models import UserManager

class CustomUserManager(UserManager):
    def create_user(self, email, username, password, **other_fields):
        if not email:
            raise ValueError("You must provide an email address")
        if not username:
            raise ValueError("You must provide a username")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user