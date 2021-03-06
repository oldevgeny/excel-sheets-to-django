# Generated by Django 3.2.3 on 2021-05-21 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input_tables', '0003_rename_pdf_table_excel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='author',
        ),
        migrations.RemoveField(
            model_name='table',
            name='cover',
        ),
        migrations.AddField(
            model_name='table',
            name='excel_to_table_image',
            field=models.ImageField(blank=True, null=True, upload_to='tables/excel_to_table_image/'),
        ),
        migrations.AddField(
            model_name='table',
            name='time',
            field=models.DateTimeField(auto_now=True, verbose_name='Uploading date'),
        ),
    ]
