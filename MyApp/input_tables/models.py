from django.db import models


class Table(models.Model):
    title = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=True, verbose_name="Uploading date")
    excel = models.FileField(upload_to='tables/excels/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.excel.delete()
        super().delete(*args, **kwargs)
