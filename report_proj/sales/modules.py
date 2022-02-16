import pandas as pd
import csv

from django.http import JsonResponse
from django.utils.dateparse import parse_date

from .db_modules import (
    get_salesman_name_from_salesman_id,
    get_customer_name_from_customer_id,
    get_sale_queryset_by_time_period,
    get_or_create_new_csv,
    get_or_create_sale,
    get_product, create_position,
)


def get_sales_data_frame(date_to, date_from):

    sales_queryset = get_sale_queryset_by_time_period(date_to, date_from)

    if len(sales_queryset):

        sales_data_frame = SalesDataFrame(sales_queryset)

        sales_data_frame.change_customer_id_to_customer_name()
        sales_data_frame.change_salesman_id_to_salesman_name()
        sales_data_frame.change_date_field_format('created', '%Y-%m-%d')
        sales_data_frame.rename_id_to_sales_id()

        return sales_data_frame.get_data_frame()
    else:
        return None


class SalesDataFrame:

    def __init__(self, sales_queryset):
        self.sales_data_frame = pd.DataFrame(sales_queryset.values())

    def change_customer_id_to_customer_name(self):
        self.sales_data_frame['customer_id'] = self.sales_data_frame['customer_id']. \
            apply(get_customer_name_from_customer_id)
        self.sales_data_frame.rename({'customer_id': 'customer_name'}, axis=1, inplace=True)

    def change_salesman_id_to_salesman_name(self):
        self.sales_data_frame['salesman_id'] = self.sales_data_frame['salesman_id']. \
            apply(get_salesman_name_from_salesman_id)
        self.sales_data_frame.rename({'salesman_id': 'salesman_name'}, axis=1, inplace=True)

    def change_date_field_format(self, data_frame_field, date_format):
        if data_frame_field == 'created' or data_frame_field == 'updated':
            self.sales_data_frame[data_frame_field] = self.sales_data_frame[data_frame_field].\
                apply(lambda x: x.strftime(date_format))
        else:
            print(data_frame_field + 'не является полем формата даты')

    def rename_id_to_sales_id(self):
        self.sales_data_frame.rename({'id': 'sales_id'}, axis=1, inplace=True)

    def get_data_frame(self):
        return self.sales_data_frame


def get_positions_data_frame(date_to, date_from):

    sales_queryset = get_sale_queryset_by_time_period(date_to, date_from)

    if len(sales_queryset):

        positions_data = get_positions_data_from_sales(sales_queryset=sales_queryset)

        positions_data_frame = pd.DataFrame(positions_data)

        return positions_data_frame
    else:
        return None


def get_positions_data_from_sales(sales_queryset):

    positions_data = []
    for sale in sales_queryset:
        for position in sale.get_positions():
            position_data = {
                'position_id': position.id,
                'product': position.product.name,
                'quantity': position.quantity,
                'price': position.price,
                'sales_id': position.get_sales_id()
            }
            positions_data.append(position_data)

    return positions_data


def create_sale_from_csv(csv_file, csv_file_name, user):
    new_csv, created = get_or_create_new_csv(csv_file_name)

    if created:
        new_csv.csv_file = csv_file
        new_csv.save()
        with open(new_csv.csv_file.path, 'r') as path:
            reader = csv.reader(path)
            reader.__next__()
            for row in reader:
                data = "".join(row).split(';')
                data.pop()

                transaction_id = data[1]
                product_name = data[2]
                quantity = int(data[3])
                customer_name = data[4]
                date = parse_date(data[5])

                product = get_product(product_name)

                if product is not None:
                    position = create_position(product, quantity, date)
                    sale, _ = get_or_create_sale(transaction_id, customer_name, date, user)
                    sale.positions.add(position)
                    sale.save()
        return JsonResponse({'was_existing': False})
    else:
        return JsonResponse({'was_existing': True})
