from django.contrib import admin

# Register your models here.
from ice_shop.models import Icecream, Category, Shop

admin.site.register(Icecream)
admin.site.register(Category)
admin.site.register(Shop)