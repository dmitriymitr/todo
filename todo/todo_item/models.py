from django.db import models


class ItemModel(models.Model):
    """
    Модель списка дел
    """
    name = models.CharField(max_length=128, verbose_name='Изменение списка')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    list_model = models.CharField(max_length=256, verbose_name='Список')
    is_done = models.BooleanField(default=False)
    expare_date = models.DateTimeField(blank=True)

    class Meta:
        verbose_name = 'Необходимо сделать'
        verbose_name_plural = 'Необходимо сделать'
