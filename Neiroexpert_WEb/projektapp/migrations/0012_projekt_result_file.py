# Generated by Django 3.1.7 on 2021-04-06 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projektapp', '0011_auto_20210406_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='projekt',
            name='result_file',
            field=models.FileField(blank=True, upload_to='isxod_dannie/', verbose_name='файл с результатами расчетов'),
        ),
    ]
