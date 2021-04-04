from django.db import models


from django.conf import settings


class Projekt (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name= 'projekt' )
    projekt_number = models.PositiveIntegerField(verbose_name= 'номер проекта' , default=1, unique=True, blank = False )
    description = models.CharField(verbose_name= 'Описание проекта', max_length=255, unique=True, blank = False)
    document = models.FileField(verbose_name= 'файл с исходными данными', upload_to='isxod_dannie/')
    add_datetime = models.DateTimeField(verbose_name= 'время' , auto_now_add= True )