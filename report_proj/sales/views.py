import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import Sale
from .forms import SalesSearchForm
from .modules import get_sales_data_frame, get_positions_data_frame, create_sale_from_csv
from .utils import get_chart

from reports.forms import ReportForm


def home_view(request):
    search_form = SalesSearchForm(request.POST or None)
    report_form = ReportForm

    sales_data_frame_html_code = None
    positions_data_frame_html_code = None
    sales_and_position_merged_data_frame_html_code = None
    grouped_by_price_data_frame_html_code = None
    chart = None
    no_data = None

    if request.method == 'POST':

        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')

        sales_data_frame = get_sales_data_frame(date_to=date_to, date_from=date_from)
        positions_data_frame = get_positions_data_frame(date_to=date_to, date_from=date_from)

        if sales_data_frame is not None:
            sales_data_frame_html_code = sales_data_frame.to_html()
            positions_data_frame_html_code = positions_data_frame.to_html()

            sales_and_position_merged_data_frame = pd.merge(sales_data_frame, positions_data_frame, on='sales_id')
            grouped_by_price_data_frame = sales_and_position_merged_data_frame.\
                groupby('transaction_id', as_index=False)['price'].agg('sum')

            sales_and_position_merged_data_frame_html_code = sales_and_position_merged_data_frame.to_html()
            grouped_by_price_data_frame_html_code = grouped_by_price_data_frame.to_html()

            chart_type = request.POST.get('chart_type')
            results_by = request.POST.get('results_by')
            print(results_by)
            chart = get_chart(chart_type, sales_data_frame, results_by)
        else:
            no_data = "No data is available in this data range"

    context = {
        'search_form': search_form,
        'report_form': report_form,
        'no_data': no_data,
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


class UploadTemplateView(TemplateView):
    template_name = 'sales/from_file.html'


def csv_upload_view(request):
    if request.method == 'POST':
        csv_file_name = request.FILES.get('file').name
        csv_file = request.FILES.get('file')
        create_sale_from_csv(csv_file, csv_file_name, request.user)


    return HttpResponse()

