import pandas as pd

from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import Table_Form
from .models import Table
from .utils import excel_to_html_table

def excel_to_table(request):
    df = excel_to_html_table()
    return render(request, 'table_list_df.html', {'table_to_html': df})

def delete_tables(request, pk):
    if request.method == 'POST':
        table = Table.objects.get(pk=pk)
        table.delete()
    return redirect('table_list')

class Table_List_View(ListView):
    model = Table
    template_name = 'table_list.html'
    context_object_name = 'tables'


class Upload_Table_View(CreateView):
    model = Table
    form_class = Table_Form
    success_url = reverse_lazy('table_list')
    template_name = 'upload_table.html'
