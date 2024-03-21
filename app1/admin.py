from django.contrib import admin
from .models import CategoryModel, GoodTypeModel

admin.site.register(CategoryModel)
admin.site.register(GoodTypeModel)