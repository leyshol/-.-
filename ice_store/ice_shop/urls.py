from django.urls import path

from ice_shop.views import index, shop

urlpatterns = [
    path('',index,name='index'),
    path('shop/<int:store_id>',shop)
]