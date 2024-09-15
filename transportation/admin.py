from django.contrib import admin

from .models import Transportation

@admin.register(Transportation)
class TransportationAdmin(admin.ModelAdmin):
    pass

