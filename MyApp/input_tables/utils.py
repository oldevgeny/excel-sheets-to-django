import pandas as pd
import numpy as np

import os

from django.conf import settings
from .models import Table


def file_names_list():
    file_names_list = []
    tables = Table.objects.all()
    for i in range(len(tables)):
        table = tables[i]
        if table.excel:
            file_names_list.append(table.excel)
    return file_names_list


def excel_to_html_table():
    list_of_names = file_names_list()
    htmls_str = ""
    for ind in range(len(list_of_names)):
        try:
            print(list_of_names[ind])
            file_name = str(list_of_names[ind])
            file_path = os.path.join(settings.BASE_DIR, 'media/' + file_name)
            print(file_path)
            xl = pd.ExcelFile(file_path)
            sheetNames = xl.sheet_names

            df = xl.parse(sheetNames[0])
            df.replace(np.nan, '-', inplace=True)
            df = df.to_html(index=False)
            htmls_str += df
        except FileNotFoundError:
            pass
        except ValueError:
            pass
            htmls_str += """
            <p class="font-weight-bold">
                There should have been a table formed from your file.
                But file is not a recognized excel file.
                Please, delete your last file and upload correct file.
            </p>"""
    return htmls_str
