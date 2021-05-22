from django.urls import path

from input_tables import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('tables/<int:pk>/', views.delete_tables, name='delete_tables'),
    path('tables/excel-to-table/', views.excel_to_table, name='to_table'),

    path('tables/', views.TableListView.as_view(), name='table_list'),
    path('tables/upload/', views.UploadTableView.as_view(), name='class_upload_table'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
