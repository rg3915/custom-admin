from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser):
    """
    This is an adaptation of Django's AbstractUser Class
    """
    email = models.EmailField(
        _('email'),
        unique=True,
        help_text=_(
            'Required (use a valid email address).'),
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ('email',)
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    @property
    def is_staff(self):
        return True
