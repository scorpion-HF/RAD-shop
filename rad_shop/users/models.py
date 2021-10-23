from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.urls import reverse
from django.utils import timezone
from branches.models import Branch


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        user.role = '0'
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True, verbose_name='پست الکترونیک')
    first_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='نام')
    last_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='نام خانوادگی')
    phone_number = models.CharField(max_length=11, blank=True, null=True, verbose_name='شماره تلفن همراه')
    address = models.TextField(null=True, blank=True, verbose_name='آدرس')
    postal_code = models.CharField(max_length=10, null=True, blank=True, verbose_name='کد پستی')
    is_staff = models.BooleanField(default=False, verbose_name='کاربر ادمین')
    is_superuser = models.BooleanField(default=False, verbose_name='کاربر مدیر')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    last_login = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ آخرین ورود')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return reverse('users:profile')

    def get_full_name(self):
        if self.is_superuser:
            return 'مدیر سایت'
        else:
            if self.first_name and self.last_name:
                return "{} {}".format(self.first_name, self.last_name)
            else:
                return None