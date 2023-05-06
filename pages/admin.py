from django.contrib import admin
from .models import *


class HomeProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "type",
    )
    search_fields = [
        "id",
        "product__product_name",
        "type",
    ]
    raw_id_fields = ("product",)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "subject",
    )
    search_fields = [
        "id",
        "name",
        "email",
        "subject",
    ]


admin.site.register(Review, ReviewAdmin)
admin.site.register(HomeProduct, HomeProductAdmin)
