from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from libgravatar import Gravatar


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

    def gravatar(self, size=120):
        """Return a URL to the user's gravatar."""
        gravatar_object = Gravatar(self.email)
        gravatar_url = gravatar_object.get_image(size=size, default='mp')
        return gravatar_url

    def mini_gravatar(self):
        """Return a URL to a miniature version of the user's gravatar."""
        return self.gravatar(size=60)

class Post(models.Model):
    author = models.ForeignKey(
        'User',
        on_delete = models.CASCADE,
        blank = False
    )
    text = models.CharField(
        max_length = 280
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        editable = False
    )

    class Meta:
        ordering = ['-created_at']
