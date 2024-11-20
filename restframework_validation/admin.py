from django.contrib import admin
from .models import Number

# Register your models here.
@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    list_display = ['even_field',]

