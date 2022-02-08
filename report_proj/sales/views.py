import pandas as pd
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Sale
from .forms import SalesSearchForm
from .modules import get_sales_data_frame, get_positions_data_frame
from .utils import get_chart


def home_view(request):
    form = SalesSearchForm(request.POST or None)

    sales_data_frame_html_code = None
    positions_data_frame_html_code = None
    sales_and_position_merged_data_frame_html_code = None
    grouped_by_price_data_frame_html_code = None
    chart = None

    if request.method == 'POST':

        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')

        sales_data_frame = get_sales_data_frame(date_to=date_to, date_from=date_from)
        positions_data_frame = get_positions_data_frame(date_to=date_to, date_from=date_from)
        sales_and_position_merged_data_frame = pd.merge(sales_data_frame, positions_data_frame, on='sales_id')
        grouped_by_price_data_frame = sales_and_position_merged_data_frame.\
            groupby('transaction_id', as_index=False)['price'].agg('sum')

        sales_data_frame_html_code = sales_data_frame.to_html()
        positions_data_frame_html_code = positions_data_frame.to_html()
        sales_and_position_merged_data_frame_html_code = sales_and_position_merged_data_frame.to_html()
        grouped_by_price_data_frame_html_code = grouped_by_price_data_frame.to_html()

        chart_type = request.POST.get('chart_type')
        chart_labels = grouped_by_price_data_frame['transaction_id'].values
        chart = get_chart(chart_type, grouped_by_price_data_frame, labels=chart_labels)

    context = {
        'form': form,
        'sales_data_frame_html_code': sales_data_frame_html_code,
        'positions_data_frame_html_code': positions_data_frame_html_code,
        'sales_and_position_merged_data_frame_html_code': sales_and_position_merged_data_frame_html_code,
        'grouped_by_price_data_frame_html_code': grouped_by_price_data_frame_html_code,
        'chart': chart
    }
    return render(request, 'sales/home.html', context=context)


class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'
    context_object_name = 'sales'


class SaleDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'
    context_object_name = 'sale'

