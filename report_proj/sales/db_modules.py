from customers.models import Customer
from profiles.models import Profile

from .models import Sale


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
