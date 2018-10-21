from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Account(AbstractUser):
    """
    Inheriting from AbstractUser instead of AbstractBaseUser
    since it has authentication and validation predefined.
    """

    def __str__(self):
        return "Account: (id={}, username={})".format(self.id, self.username)