from django.contrib import admin
from .models import Product, Category, ProductInventory, SupplierProduct

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "sale_price",  "is_perishable", "explation_date", "enabled"]
    exclude = ["slug"]
    search_fields = ["name"]
    list_display_links = ["name"]
    list_editable = ["sale_price", "is_perishable", "explation_date", "enabled"]
    list_per_page = 100
    list_max_show_all = 1000


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]
    list_display_links = ["name"]
    list_per_page = 100
    list_max_show_all = 1000


@admin.register(SupplierProduct)
class SupplierProduct(admin.ModelAdmin):
    list_display = ["id", "product", "supplier", "cost_price"]
    search_fields = ["product"]
    list_per_page = 100
    list_max_show_all = 1000   
    
@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    list_display = ["id", "quantity"]
    search_fields = ["quanity"]
    list_per_page = 100
    list_max_show_all = 1000