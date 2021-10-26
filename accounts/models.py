from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext as _
from phone_field import PhoneField


class UserManager(BaseUserManager):
    def create_user(self, username, email, profile_name, phone, password=None):
        if not username:
            raise ValueError(_('Должно быть имя пользователя'))
        if not email:
            raise ValueError(_('Пользователь должен иметь адрес электронной почты'))
        if not profile_name:
            raise ValueError(_('Должно быть имя'))
        if not phone:
            raise ValueError(_('Должно быть телефон'))

        user = self.model(username=username, profile_name=profile_name, phone=phone, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, profile_name, phone, password=None):
        user = self.create_user(username, email, profile_name, phone, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


# User модель
class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('NOT_DEFINED', 'Не указано'),
        ('MALE', 'Мужской'),
        ('FAMALE', 'Женский'),
    )

    username = models.CharField(verbose_name=_('username'), max_length=32, unique=True)
    email = models.EmailField(verbose_name=_('email address'), max_length=64, unique=True)
    profile_name = models.CharField(verbose_name=_('Полная имя'), max_length=64)
    gender = models.CharField(verbose_name='Пол', max_length=12, choices=GENDER_CHOICES, default=GENDER_CHOICES[0][1])
    phone = PhoneField(verbose_name=_('Телефон'), help_text='Контакт телефона')
    birthday = models.DateField(verbose_name=_('Дата рождение'), blank=True, null=True)

    is_active = models.BooleanField(verbose_name=_('Статус активность'), help_text='Это статус активности пользователя.', default=True)
    is_staff = models.BooleanField(verbose_name=_('Статус партнера'), help_text='Статус бренда как нашего партнера.', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'profile_name', 'phone',]

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username


    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'