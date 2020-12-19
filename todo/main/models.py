from django.db import models


class List(models.Model):
    """
    Модель списка дел
    """
    name = models.CharField(max_length=128, verbose_name='Изменение списка')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Список дел'
        verbose_name_plural = 'Список дел'
        unique_together = ('name', 'user')
