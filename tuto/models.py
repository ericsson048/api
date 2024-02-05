from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

class UserProfilesManager(BaseUserManager):

    """ model for manage user profiles """

    def create_user(self, Email, FirstName, LastName, password=None):
        """ creation of a new user profile """
        if not Email:
            raise ValueError('a user must have an email address')

        Email=self.normalize_email(Email)
        user=self.model(Email=Email, FirstName=FirstName, LastName=LastName)

        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_superuser(self,Email, FirstName, LastName, Password):

        """creation a superuser with the given details"""

        user=self.create_user(Email, FirstName, LastName, Password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Email=models.EmailField(max_length=255,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)

    objects= UserProfilesManager()

    USERNAME_FIELD='Email'
    REQUIRED_FIELDS=['FirstName', 'LastName']

    def get_full_name(self):
        return self.FirstName + "" + self.LastName

    def get_short_name(self):
        return self.LastName

    def __str__(self):
        return self.Email
