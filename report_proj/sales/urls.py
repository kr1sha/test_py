from django.urls import path

from .views import (
    home_view,
    SaleListView,
    SaleDetailView,
    UploadTemplateView,
    csv_upload_view,
)

app_name = 'sales'

urlpatterns = [
    path('', home_view, name='home'),
    path('from_file/', UploadTemplateView.as_view(), name='from-file'),
    path('csv_upload/', csv_upload_view, name='csv-upload'),
    path('sales/', SaleListView.as_view(), name='list'),
    path('sales/<int:pk>/', SaleDetailView.as_view(), name='detail')
]
