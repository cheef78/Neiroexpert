from django.contrib import admin

from projektapp.models import Projekt
from mainapp.models import HelpInfo

admin.site.register(Projekt)
admin.site.register(HelpInfo)

# Register your models here.
