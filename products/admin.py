from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')  # Columns displayed in the admin list view
    search_fields = ('name', 'description')  # Enable search functionality
    list_filter = ('price',)  # Add filters in the sidebar