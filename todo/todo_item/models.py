from django.db import models


class ItemModel(models.Model):
    """
    Модель списка дел
    """
    name = models.CharField(max_length=128, verbose_name='Изменение списка')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    list_model = models.ForeignKey('main.List', on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    expare_date = models.DateTimeField(blank=True)

    class Meta:
        verbose_name = 'Необходимо сделать'
        verbose_name_plural = 'Необходимо сделать'
