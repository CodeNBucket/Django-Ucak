from django.contrib import admin
from .models import Montaj

@admin.register(Montaj)
class MontajAdmin(admin.ModelAdmin):
    list_display = ('ucak', 'tarih', 'takim')  
    list_filter = ('tarih', 'takim')        
    search_fields = ('ucak__isim', 'takim__isim')  
