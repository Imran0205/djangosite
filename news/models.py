from django.db import models

# Create your models here.
class newsl(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    text = models.TextField(verbose_name='Текст')
    date = models.DateTimeField(verbose_name='Дата')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'