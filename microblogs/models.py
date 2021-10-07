from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(
        max_length = 30,
        unique = True,
        validators = [RegexValidator(
            regex=r'^@\w{3,}$',
            message='Username must consist of @ followed by at least 3 alphanumericals.'
        )]
    )

    first_name = models.CharField(
        max_length = 50,
        blank = False,
    )

    last_name = models.CharField(
        max_length = 50,
        blank = False,
    )

    email = models.EmailField(
        unique = True,
        blank = False,
        validators = [EmailValidator(
            message='Email must consist a usernamem, an @, a domain name, followed  by a dot, and a domain'
        )]
    )

    bio = models.CharField(
        default = '',
        blank = True,
        max_length = 520,
    )
