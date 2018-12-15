import binascii
import os
from django.conf import settings
from django.db import models
from tenants.models import TenantMaster
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
# Create your models here.

class ResetPasswordToken(models.Model):
    class Meta:
        verbose_name = _("Password Reset Token")
        verbose_name_plural = _("Passwrod Reset Tokens")

    @staticmethod
    def generate_key():
        return binascii.hexlify(os.urandom(32)).decode()

    id = models.AutoField( primary_key=True)

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        related_name='password_reset_tokens',
        on_delete=models.CASCADE,
        verbose_name=_("The User which is associated to this password reset token")
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("When was this token generated")
    )

    key = models.CharField(
        _("Key"),
        max_length=64,
        db_index=True,
        unique=True
    )

    ip_address = models.GenericIPAddressField(
        _("The IP address of this session"),
        default="127.0.0.1"
    )

    user_agent = models.CharField(
       max_length=256,
       verbose_name="HTTP User Agent"
    )

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(ResetPasswordToken, self).save(*args, **kwargs)
    def __str__(self):
        return "Password reset token for user {user}".format(user=self.user)

class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=UserManager.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    objects = UserManager()
    date_added = models.DateField(auto_now=False, auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    tenant = models.ForeignKey(TenantMaster, models.SET_NULL, blank=True, null=True,)
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    def get_full_name(self):
    # The user is identified by their email address
        return self.first_name + " " + self.last_name

    def get_short_name(self):
    # The user is identified by their email address
        return self.email

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):

    # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):

    # Simplest possible answer: Yes, always
        return True

    def is_staff(self):

    # Simplest possible answer: All admins are staff
        return self.is_admin

