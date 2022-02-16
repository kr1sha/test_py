from customers.models import Customer
from profiles.models import Profile
from products.models import Product

from .models import Sale, CSV, Position


def get_sale_queryset_by_time_period(date_to, date_from):
    sales_queryset = Sale.objects.filter(created__date__lte=date_to, created__date__gte=date_from)
    return sales_queryset


def get_salesman_name_from_salesman_id(salesman_id):
    salesman = Profile.objects.get(id=salesman_id)
    salesman_name = salesman.user.username
    return salesman_name


def get_customer_name_from_customer_id(customer_id):
    customer_name = Customer.objects.get(id=customer_id)
    return customer_name


def get_or_create_new_csv(csv_name):
    new_csv, created = CSV.objects.get_or_create(file_name=csv_name)
    return new_csv, created


def get_product(product_name):
    try:
        product = Product.objects.get(name=product_name)
    except Product.DoesNotExist:
        product = None

    return product


def create_position(product, quantity, date):
    position = Position.objects.create(product=product, quantity=quantity, created=date)
    return position


def get_or_create_sale(transaction_id, customer_name, date, user):
    customer, _ = Customer.objects.get_or_create(name=customer_name)
    salesman = Profile.objects.get(user=user)
    sale, _ = Sale.objects.get_or_create(transaction_id=transaction_id, customer=customer,
                                         salesman=salesman, created=date)

    return sale, _

