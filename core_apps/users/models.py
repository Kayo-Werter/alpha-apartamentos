import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.utils.translation import gettext_lazy as _
from core_apps.users.managers import UserManager


class UsernameValidator(validators.RegexValidator):
    regex = r"^[\w.@+-]+\Z"
    message = _("seu nome de usuário não é válido. Um nome de usuário pode conter apenas letras, números, um ponto ,@,+,-")
    flag = 0


class User(AbstractUser):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=60)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=60)
    email = models.EmailField(verbose_name=_("Email Adress"), unique=True, db_index=True)
    username = models.CharField(verbose_name=_("Username"), max_length=60, unique=True, validators=[UsernameValidator])

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-date_joined"]


    @property
    def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()