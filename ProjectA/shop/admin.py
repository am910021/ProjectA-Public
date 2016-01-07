from django.contrib import admin
from shop.models import Type, Item, Brand, Category


# Register your models here.
admin.site.register(Type)
admin.site.register(Item)
admin.site.register(Brand)
admin.site.register(Category)