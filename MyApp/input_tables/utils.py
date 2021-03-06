import pandas as pd
import numpy as np

import os

from django.conf import settings
from .models import Table


def file_names_list():
    file_names_list = []
    tables = Table.objects.all()
    for tab in tables:
        table = tab
        if table.excel:
            file_names_list.append(table.excel)
    return file_names_list


def excel_to_html_table():
    list_of_names = file_names_list()
    htmls_list = []
    for name in list_of_names:
        try:
            file_name = str(name)
            file_path = os.path.join(settings.BASE_DIR, 'media/' + file_name)
            xl = pd.ExcelFile(file_path)
            sheetNames = xl.sheet_names

            df = xl.parse(sheetNames[0])
            df.replace(np.nan, '-', inplace=True)
            df = df.to_html(index=False)
            htmls_list.append(df)
            htmls_list.append('<hr>')
        except FileNotFoundError:
            pass
        except ValueError:
            pass
            htmls_list.append("""
            <p class="font-weight-bold">
                There should have been a table formed from your file.
                But file is not a recognized excel file.
                Please, delete your last file and upload correct file.
            </p>
            <hr>""")
    return ''.join(htmls_list)
