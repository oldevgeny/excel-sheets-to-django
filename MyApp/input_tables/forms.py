from django import forms

from .models import Table


class Table_Form(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('excel',)
