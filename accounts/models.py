from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext as _



class BrandManager(BaseUserManager):
    def create_user(self, brandname, email, password=None):
        if not brandname:
            raise ValueError(_('Должно быть название бренда'))
        if not email:
            raise ValueError(_('Бренд должен иметь адрес электронной почты'))

        store = self.model(brandname = brandname, email = self.normalize_email(email))
        store.set_password(password)
        store.save()
        return store

    def create_superuser(self, brandname, email, password=None):
        store = self.create_user(brandname, email, password=password)
        store.is_superuser = True
        store.is_staff = True
        store.save()
        return store

# Our Store model
class Brand(AbstractBaseUser, PermissionsMixin):
    brandname = models.CharField(verbose_name=_('Имя бренда'), max_length=64, unique=True)
    email = models.EmailField(verbose_name=_('email address'), max_length=255, unique=True)
    is_active = models.BooleanField(verbose_name=_('Статус активность'), help_text='Это статус активности пользователя.', default=True)
    is_staff = models.BooleanField(verbose_name=_('Статус партнера'), help_text='Статус бренда как нашего партнера.', default=False)

    objects = BrandManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['brandname']

    def __str__(self):
        return self.brandname

    def get_full_name(self):
        return self.brandname

    def get_short_name(self):
        return self.brandname

    def delete(self, *args, **kwargs):
        for product in self.product_set.all():
            product.delete()
        super().delete(*args, **kwarg)

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'