from django.db import models

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField("email", unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'users'


User._meta.get_field('user_permissions').remote_field.related_name = 'user_user_permissions'
User._meta.get_field('groups').remote_field.related_name = 'user_groups'


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        db_table = 'customers'


class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'
        db_table = 'vendors'



class Service(models.Model):
    SERVICE_TYPES = [
        ('birthday', 'Birthday Shoot'),
        ('prewedding', 'Pre-Wedding Shoot'),
        ('wedding', 'Wedding Shoot'),
        ('event', 'Event'),
    ]

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='services')
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.get_service_type_display()} - {self.vendor.user.email}"

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        db_table = 'services'
