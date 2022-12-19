from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField


class UserRoles:

    USER = "user"
    ADMIN = "admin"
    ROLE = [(USER, "user"), (ADMIN, "admin")]


class User(AbstractUser):

    objects = UserManager()

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    email = models.EmailField(max_length=254, unique=True, verbose_name='Почта')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, blank=True, verbose_name='Фамилия')
    password = models.CharField(max_length=128, verbose_name='Пароль')
    phone = PhoneNumberField(null=True, blank=True, verbose_name='Телефон')
    role = models.CharField(max_length=100, choices=UserRoles.ROLE, default=UserRoles.USER, verbose_name='Роль')
    image = models.ImageField(upload_to='django_media/', null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['email']

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    def __str__(self):
        return self.email
