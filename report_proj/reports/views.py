from django.shortcuts import render
from django.http import JsonResponse

from profiles.models import Profile

from .utils import is_ajax, get_report_image
from .models import Report


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