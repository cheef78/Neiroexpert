from django.db import models

# Create your models here.
from django.conf import settings

class HelpInfo (models.Model):
    init_file = models.FileField(verbose_name= 'файл с исходными данными', upload_to='help_materials/', blank = True)
    init_create = models.FileField(verbose_name= 'файл с с описанием программы и процесса регистрации', upload_to='help_materials/', blank = True)
    projekt_create_activate = models.FileField(verbose_name= 'файл с с описанием создания проекта и его активации', upload_to='help_materials/', blank = True)
    projekt_neiro_calc = models.FileField(verbose_name= 'файл с с описанием выполнения расчета и его результатов', upload_to='help_materials/', blank = True)
    