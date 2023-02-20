from django.db import models


class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=258, verbose_name='Токен')
    tg_chat = models.CharField(max_length=258, verbose_name='Чат айди')
    tg_message = models.TextField(max_length=258, verbose_name='Сообщение')

    def __str__(self):
        return self.tg_chat

    class Meta:
        verbose_name = 'Настройку'
        verbose_name_plural = 'Настройки'
