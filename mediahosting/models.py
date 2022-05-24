from django.db import models
from accounts.models import User

# class Post(models.Model):
#     title = models.CharField(verbose_name='Название', max_length=64)
#     description = models.TextField(verbose_name='Описание')
#     owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
#     date_created = models.DateTimeField(verbose_name='Дата выхода', auto_now_add=True)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Пост'
#         verbose_name_plural = 'Посты'
#         ordering = ['-date_created']