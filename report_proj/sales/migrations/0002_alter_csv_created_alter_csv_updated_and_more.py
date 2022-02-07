# Generated by Django 4.0.1 on 2022-02-01 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='csv',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Время последнего обновления'),
        ),
        migrations.AlterField(
            model_name='position',
            name='created',
            field=models.DateTimeField(blank=True, verbose_name='Время создания позиции'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='created',
            field=models.DateTimeField(blank=True, verbose_name='Дата начала сделки'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления сделки'),
        ),
    ]