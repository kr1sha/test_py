from django.db import models
from django.utils import timezone
from django.shortcuts import reverse

from products.models import Product
from customers.models import Customer
from profiles.models import Profile

from .utils import generate_code


class Position(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Наименование товара')
    quantity = models.PositiveIntegerField(verbose_name='Колличество товара')
    price = models.FloatField(blank=True, verbose_name='Цена позиции')
    created = models.DateTimeField(blank=True, verbose_name='Время создания позиции')

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        return super().save(*args, **kwargs)

    def get_price(self):
        return self.price

    def get_sales_id(self):
        sale_object = self.sale_set.first()
        return sale_object.id

    def __str__(self):
        return f"id: {self.pk}, product: {self.product.name}, quantity: {self.quantity}"


class Sale(models.Model):
    transaction_id = models.CharField(max_length=12, blank=True, verbose_name="id транзакции")
    positions = models.ManyToManyField(Position, verbose_name="Позиции")
    total_price = models.FloatField(blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Покупатель')
    salesman = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Продавец')
    created = models.DateTimeField(blank=True, verbose_name='Дата начала сделки')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления сделки')

    def save(self, *args, **kwargs):
        if self.transaction_id == "":
            self.transaction_id = generate_code()

        if self.created is None:
            self.created = timezone.now()

        return super().save(*args, **kwargs)

    def get_positions(self):
        return self.positions.all()

    def __str__(self):
        return f"Sales for the amount of ${self.total_price}"

    def get_absolute_url(self):
        return reverse('sales:detail', kwargs={'pk': self.pk})



class CSV(models.Model):
    file_name = models.FileField(upload_to='csvs', verbose_name='Имя файла')
    is_activated = models.BooleanField(default=False, verbose_name='Активирован ли')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Время последнего обновления')

    def __str__(self):
        return str(self.file_name)



