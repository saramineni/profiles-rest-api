from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """helps django work with custom user models"""

    def create_user(self, email, name, password= None):
        """creates user profile object"""
        if not email:
            raise ValueError('email field cannot be empty')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """helps in creating super user"""

        user = self.create_user(email, name, password)
        user.is_superuser= True
        user.is_staff=True
        user.save(using=self._db)

class UserProfile(AbstractBaseUser,PermissionsMixin):

    """Represents a user profile inside your system"""

    email = models.EmailField(max_length=255, unique=True)
    name= models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_Active= models.BooleanField(default= True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        """get the user profile user name"""

        return self.name

    def get_short_name(self):
        """get the users short name"""
        return self.name

    def __str__(self):
        return self.email

 
