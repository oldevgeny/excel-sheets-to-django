from django.db import models


class Table(models.Model):
    title = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=True, verbose_name="Uploading date")
    excel = models.FileField(upload_to='tables/excels/')
    excel_to_table_image = models.ImageField(upload_to='tables/excel_to_table_image/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.excel.delete()
        self.excel_to_table_image.delete()
        super().delete(*args, **kwargs)
