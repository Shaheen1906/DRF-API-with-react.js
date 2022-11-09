from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','product_name','price','quantity')