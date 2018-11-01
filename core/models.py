from django.db import models


class RhubarbTask(models.Model):
    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'
        ordering = 'created',

    created = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)

    name = models.CharField(verbose_name='название задачи', max_length=128)
    params = models.TextField(verbose_name='параметры', help_text='JSON, удовлетворяющий схеме задачи.')

    result = models.TextField(verbose_name='результат выполнения', blank=True, null=True)
    is_done = models.BooleanField(verbose_name='выполнена?', default=False)
    email = models.EmailField(verbose_name='email получателя', blank=True, null=True)

    def __str__(self):
        return f'{self.name} от {self.created}'

