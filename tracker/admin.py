from django.contrib import admin
from .models import *
# Register your models here.
class TrackDataAdmin(admin.ModelAdmin):

  list_display = ('email', 'timestamp')

admin.site.register(EmailTracking, TrackDataAdmin)