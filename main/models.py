from django.db import models

# Create your models here.
class advices(models.Model):
    Name = models.CharField(verbose_name='Имя', max_length=100)
    Advice = models.TextField(verbose_name='Совет')
    class Meta:
        verbose_name = 'Совет'
        verbose_name_plural = 'Советы'

class langmod(models.Model):
    lang = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание')
    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'