# Generated by Django 3.1.4 on 2021-01-09 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201216_1911'),
        ('todo_item', '0003_auto_20201220_1341'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemmodel',
            options={'verbose_name': 'Элемент списка', 'verbose_name_plural': 'Элементы списка'},
        ),
        migrations.AlterField(
            model_name='itemmodel',
            name='expare_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='itemmodel',
            unique_together={('name', 'list_model')},
        ),
    ]
