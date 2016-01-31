from django.contrib import admin
from account.models import Profile, GroupOrder, Order, MyCart


admin.site.register(Profile)
admin.site.register(GroupOrder)
admin.site.register(Order)
admin.site.register(MyCart)