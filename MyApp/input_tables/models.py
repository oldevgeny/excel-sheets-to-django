from django.db import models


class Table(models.Model):
    time = models.DateTimeField(auto_now=True, verbose_name="Uploading date")
    excel = models.FileField(upload_to='tables/excels/')

    def delete(self, *args, **kwargs):
        self.excel.delete()
        super().delete(*args, **kwargs)
