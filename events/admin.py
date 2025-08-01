from django.contrib import admin

# Register your models here.
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'location')
    search_fields = ('title', 'location')