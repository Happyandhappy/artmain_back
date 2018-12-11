from django.db import models

# Create your models here.
from tenant_schemas.models import TenantMixin
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class TenantMaster(TenantMixin):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    company_description = models.TextField(default="")
    company_address = models.CharField(max_length=200, default="")
    company_city = models.CharField(max_length=200, default="")
    contry_code = models.CharField(max_length=200, default="")
    company_phone = models.CharField(max_length=200, default="")
    company_email = models.EmailField(blank=True, null=True)
    company_contact = models.CharField(max_length=200, default="")
    company_active = models.BooleanField(default=False)
    control = models.CharField(max_length=100, default="")
    created_on = models.DateField(auto_now_add=True)
    auto_create_schema = True

    def __unicode__(self):
        return self.company_name

    def __str__(self):
        return self.company_name

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
    email = models.EmailField(db_index=True)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        unique_together = ('tenant', 'email',)

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

