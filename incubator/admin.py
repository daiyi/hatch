from django.contrib import admin

from .models import Egg, Incubator

admin.site.register(Incubator)
admin.site.register(Egg)

