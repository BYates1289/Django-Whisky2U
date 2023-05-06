from django.contrib import admin
from .models import Category, Product, Rating


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    search_fields = [
        "id",
        "name",
    ]


class RatingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "product",
    )
    search_fields = [
        "id",
        "user__email",
        "product__product_name",
        "star",
    ]
    raw_id_fields = (
        "user",
        "product",
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_name",
        "type",
        "price",
    )
    search_fields = [
        "id",
        "product_name",
        "type",
        "price",
    ]
    raw_id_fields = ("category",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Rating, RatingAdmin)
