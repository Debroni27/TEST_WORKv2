from django.contrib import admin

from product.models import ProductImage, Product
from core.utils import CachingPaginator


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'part_number', 'price')
    list_display_links = ('name', )
    search_fields = ('name', 'part_number')
    list_filter = ('status', )
    list_per_page = 10
    inlines = [ProductImageAdmin, ]
    show_full_result_count = False
    paginator = CachingPaginator
