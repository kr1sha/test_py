from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from profiles.models import Profile

from .utils import is_ajax, get_report_image
from .models import Report


class ReportListView(ListView):
    model = Report
    template_name = 'reports/report_list.html'
    context_object_name = 'reports'


class ReportDetailView(DetailView):
    model = Report
    template_name = 'reports/report_detail.html'
    context_object_name = 'report'


def create_report_view(request):
    if is_ajax(request):
        name = request.POST.get('name')
        remark = request.POST.get('remarks')
        string_img = request.POST.get('image')

        image = get_report_image(string_img)
        author = Profile.objects.get(user=request.user)

        Report.objects.create(name=name, image=image, remark=remark, author=author)
        return JsonResponse({'msg': 'send'})

    return JsonResponse({})


def render_pdf_view(request, pk):
    template_path = 'reports/pdf.html'
    report = get_object_or_404(Report, pk=pk)
    context = {'report': report}

    response = HttpResponse(content_type='application/pdf')
    # if download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display
    response['Content-Disposition'] = 'filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
       html, dest=response)

    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
