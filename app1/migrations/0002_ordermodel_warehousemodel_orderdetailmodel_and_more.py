# Generated by Django 4.2.11 on 2024-03-21 19:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('order_date', models.DateTimeField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=100)),
                ('warehouse_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetailModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('good_type_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.goodtypemodel')),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.ordermodel')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsOnWarehouseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_type_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.goodtypemodel')),
                ('warehouse_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.warehousemodel')),
            ],
        ),
    ]