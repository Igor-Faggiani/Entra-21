from django.contrib import admin
from .models import Supplier

# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ["id", "comany_name", "fantasy_name", "email", "enabled"]
    exclude = ["slug"]
    ordering = ["id"]
    list_filter = ["enabled", "created_at"]
    search_fields = ["company_name", "email"]
    list_display_fields = ["company_name"]
    list_editable = ["fantasy_name", "enabled"]
    list_per_page = 100
    list_max_show_all = 1000