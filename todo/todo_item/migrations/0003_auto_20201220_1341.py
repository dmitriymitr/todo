# Generated by Django 3.1.4 on 2020-12-20 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201216_1911'),
        ('todo_item', '0002_itemmodel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemmodel',
            name='user',
        ),
        migrations.AlterField(
            model_name='itemmodel',
            name='list_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.list'),
        ),
    ]
