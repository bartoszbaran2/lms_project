from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, Group
from django.db import models


class AccountManager(BaseUserManager):
    def create_user(self, email, fullname, password=None):
        if not email:
            raise ValueError('no email')

        user = self.model(email=self.normalize_email(email), fullname=fullname) # zawsze tak
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)

        if not user.is_instructor:
            instructor_group = Group.objects.get(name='students')
            user.groups.add(instructor_group)

        return user

    def create_superuser(self, email, fullname, password=None):
        user = self.create_user(email=self.normalize_email(email), fullname=fullname)

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class Accounts(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='User email', max_length=64, unique=True)
    fullname = models.CharField(max_length=32, unique=True)
    is_instructor = models.BooleanField(default=False)
    date_join = models.DateTimeField(verbose_name='Date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager() # podpięcie managera

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']

    def __str__(self):
        return self.email
