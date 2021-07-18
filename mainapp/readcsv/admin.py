from django.contrib import admin
from .models import Deals


@admin.register(Deals)
class DealsAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'item', 'total', 'quantity', 'date']
    ordering = ['id']
