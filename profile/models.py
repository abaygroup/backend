from django.db import models
from accounts.models import User
from django.core.exceptions import ValidationError


# Модель Profile
# =====================================================================================
class Profile(models.Model):

    def validate_logotype(logotype):
        filesize = logotype.size
        megabyte_limit = 2.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Максимальный размер файла должно быть %sMB" % str(megabyte_limit))

    # Направление бренда или магазина
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    avatar = models.ImageField(verbose_name='Аватар', validators=[validate_logotype], upload_to='profile/avatar/', blank=True, null=True, help_text='Максимальный размер файла 2MB')
    category = models.ForeignKey(SuperCategory, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Категория')
    body = models.TextField(verbose_name='О вас', max_length=300, blank=True, null=True)

    # Персональные данные
    address = models.TextField(verbose_name='Адрес', max_length=255, blank=True, null=True)
    # reserve_email = models.EmailField(verbose_name='Резервный email', max_length=64, blank=True, null=True)
    # website = models.CharField(verbose_name='Веб сайт', max_length=64, blank=True, null=True)

    # Статусы
    branding = models.BooleanField(verbose_name='Брендинг', default=False)


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

# =====================================================================================


class Author(models.Model):

    def validate_picture(picture):
        filesize = picture.size
        megabyte_limit = 2.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Максимальный размер файла должно быть %sMB" % str(megabyte_limit))

    picture = models.ImageField(validators=[validate_picture], upload_to='profile/authors/', blank=True, null=True, help_text='Максимальный размер файла 2MB')
    full_name = models.CharField(verbose_name='Полная имя автора', max_length=64)
    about = models.TextField(verbose_name='О авторе')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

# Уведомление
# =====================================================================================
class Notification(models.Model):
    title = models.CharField(verbose_name='Тема', max_length=64)
    body = models.TextField(verbose_name='Описание')
    to_send = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='От кого', related_name='send_to')
    from_send = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кому')
    date_send = models.DateTimeField(verbose_name='Дата отправление', auto_now_add=True)

    checked = models.BooleanField(verbose_name='Проверка', default=False)

    def __str__(self):
        return 'Отправлено из {} на {}'.format(self.to_send, self.from_send)

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомлений'
        ordering = ['-date_send']

# =====================================================================================