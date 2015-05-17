from django.contrib import admin
from models import Egg, Incubator
import time


class EggInline(admin.StackedInline):
    model = Egg
    extra = 0


@admin.register(Egg)
class EggAdmin(admin.ModelAdmin):
    list_display = ('owner', 'identity', 'steps_needed', 'steps_received', 'focus' )

    def owner(self, obj):
        return (obj.incubator.owner.username)
    owner.short_description = "Owner"

    
@admin.register(Incubator)
class IncubatorAdmin(admin.ModelAdmin):
    list_display = ('owner', 'last_updated_readable', 'last_updated')
    inlines = [EggInline]

    def last_updated_readable(self, obj):
        return (time.ctime(obj.last_updated))
    last_updated_readable.short_description = "Last updated, human readable"
