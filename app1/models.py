import uuid
import datetime
from django.db import models
from django.contrib.auth.models import User


class GoodTypeModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    category = models.ForeignKey("CategoryModel", null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    image = models.ImageField()
    is18 = models.BooleanField()
    expiration_date = models.DurationField(null=True, default=datetime.timedelta(days=730))

    def __str__(self):
        return self.name


class CategoryModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class OrderModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    order_date = models.DateTimeField()
    user_id = models.ForeignKey("User", on_delete=models.SET_NULL)
    status = models.CharField(max_length=50)
    number = models.AutoField()

    def __str__(self):
        return f"Order #{self.number}"


class OrderDetailModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    order_id = models.ForeignKey("OrderModel", on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    good_type_id = models.ForeignKey("GoodTypeModel", on_delete=models.SET_NULL)


class GoodsOnWarehouseModel(models.Model):
    good_type_id = models.ForeignKey("GoodTypeModel", on_delete=models.SET_NULL)
    warehouse_id = models.ForeignKey("WarehouseModel", on_delete=models.SET_NULL)


class WarehouseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    address = models.CharField(max_length=100)
    warehouse_name = models.CharField(max_length=50)

    def __str__(self):
        return self.warehouse_name

