

from django.conf import settings
from django.db import models

from users.models import User


class Ad(models.Model):

    title = models.CharField(max_length=100, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    description = models.CharField(max_length=800, blank=True, null=True, verbose_name='Описание')
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    image = models.ImageField(upload_to="images/", verbose_name="фото", null=True, blank=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ("-created_at",)


class Comment(models.Model):

    text = models.CharField(max_length=100, verbose_name='Комментарий')
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ("-created_at",)

