from django.contrib import admin

from .models import Product, Stock, StockProduct


class StockProductInLine(admin.TabularInline):
    model = StockProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    inlines = [StockProductInLine]
