from django.contrib import admin
from account.models import UserProfile, GroupOrder, Order, MyCart


admin.site.register(UserProfile)
admin.site.register(GroupOrder)
admin.site.register(Order)
admin.site.register(MyCart)