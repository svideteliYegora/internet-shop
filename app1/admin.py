from django.contrib import admin
from .models import CategoryModel, GoodTypeModel, OrderModel, OrderDetailModel, GoodsOnWarehouseModel, WarehouseModel


class GoodTypeInline(admin.TabularInline):
    model = GoodTypeModel.categories.through


@admin.register(GoodTypeModel)
class GoodTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "get_categories_display", "is18", "image"]
    fields = ["name", "categories", "description", "image", "is18"]
    list_filter = ["name", "categories", "is18"]

    def get_categories_display(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    get_categories_display.short_description = 'Categories'


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "total_price", "order_date", "status"]
    list_filter = ["order_date", "status"]


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        GoodTypeInline,
    ]


@admin.register(OrderDetailModel)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ["order_id", "quantity", "good_type_id"]


@admin.register(GoodsOnWarehouseModel)
class GoodsOnWarehouseAdmin(admin.ModelAdmin):
    list_display = ["good_type_id", "warehouse_id"]


@admin.register(WarehouseModel)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ["address", "warehouse_name"]