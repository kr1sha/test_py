# Generated by Django 4.0.1 on 2022-02-01 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0002_rename_profiles_profile'),
        ('products', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='csvs', verbose_name='Имя файла')),
                ('is_activated', models.BooleanField(default=False, verbose_name='Активирован ли')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Время создания')),
                ('updated', models.DateField(auto_now=True, verbose_name='Время последнего обновления')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Колличество товара')),
                ('price', models.FloatField(blank=True, verbose_name='Цена позиции')),
                ('created', models.DateField(blank=True, verbose_name='Время создания позиции')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Наименование товара')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(blank=True, max_length=12, verbose_name='id транзакции')),
                ('total_price', models.FloatField(blank=True)),
                ('created', models.DateField(blank=True, verbose_name='Дата начала сделки')),
                ('updated', models.DateField(auto_now=True, verbose_name='Дата последнего обновления сделки')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer', verbose_name='Покупатель')),
                ('positions', models.ManyToManyField(to='sales.Position', verbose_name='Позиции')),
                ('salesman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile', verbose_name='Продавец')),
            ],
        ),
    ]
