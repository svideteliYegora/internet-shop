# Generated by Django 4.2.11 on 2024-03-22 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_ordermodel_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodtypemodel',
            name='category',
        ),
        migrations.AddField(
            model_name='goodtypemodel',
            name='categories',
            field=models.ManyToManyField(to='app1.categorymodel'),
        ),
    ]
