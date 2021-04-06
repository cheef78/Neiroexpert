from django.db import models



from django.conf import settings

def projekt_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Projekt (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name= 'projekt' )
    projekt_number = models.PositiveIntegerField(verbose_name= 'номер проекта' , default=1, blank = False )
    description = models.CharField(verbose_name= 'Описание проекта', max_length=255, blank = False, default='жд линия А - Б')
    document = models.FileField(verbose_name= 'файл с исходными данными', upload_to='isxod_dannie/')
    add_datetime = models.DateTimeField(verbose_name= 'время' , auto_now_add= True )
    neiro_damage_result = models.FileField(verbose_name= 'файл с результатами расчетов', upload_to='isxod_dannie/', blank = True)
    neiro_damage_flag = models.BooleanField(verbose_name= 'Результат выполнения расчетов сил/повреждаемостей по нейромодели', blank = False, default=False)