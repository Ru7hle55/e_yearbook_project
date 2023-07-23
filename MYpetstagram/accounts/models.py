from enum import unique
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core import validators
from .validators import validate_only_alphabetical_letters


# Create your models here.
class PetstagramUser(AbstractUser):
    CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Do not show', 'Do not show'),
    ]

    first_name = models.CharField(
        max_length=30,
        validators=[
            validators.MinLengthValidator(2),
            validate_only_alphabetical_letters
        ],
    )
    last_name = models.CharField(
        max_length=30,
        validators=[
            validators.MinLengthValidator(2),
            validate_only_alphabetical_letters
        ],
    )
    email = models.EmailField(
        unique=True,
    )
    gender = models.CharField(
        choices=CHOICES
    )
    profile_picture = models.URLField(
    )


    def get_user_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name or self.last_name:
            return self.first_name or self.last_name
        else:
            return self.username