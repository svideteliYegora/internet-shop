import uuid
import datetime
from django.db import models


class CategoryModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class GoodTypeModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField(CategoryModel)
    image = models.ImageField(blank=True, null=True)
    is18 = models.BooleanField()
    expiration_date = models.DurationField(null=True, default=datetime.timedelta(days=730), blank=True)

    def __str__(self):
        return self.name


# class GoodTypeCategoryModel(models.Model):
#     good_type_id = models.ForeignKey("GoodTypeModel", null=True, on_delete=models.SET_NULL)
#     category_id = models.ForeignKey("CategoryModel", null=True, on_delete=models.SET_NULL)


class OrderModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Order #{self.id} + {self.order_date}"


class OrderDetailModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    order_id = models.ForeignKey("OrderModel", on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    good_type_id = models.ForeignKey("GoodTypeModel", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.order_id)


class GoodsOnWarehouseModel(models.Model):
    good_type_id = models.ForeignKey("GoodTypeModel", on_delete=models.SET_NULL, null=True)
    warehouse_id = models.ForeignKey("WarehouseModel", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.warehouse_id)


class WarehouseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    address = models.CharField(max_length=100)
    warehouse_name = models.CharField(max_length=50)

    def __str__(self):
        return self.warehouse_name

