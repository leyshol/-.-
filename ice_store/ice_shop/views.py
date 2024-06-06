from django.shortcuts import render

# Create your views here.
from ice_shop.models import Shop


def index(request):
    ctx = {
        'shops':Shop.objects.all()
    }

    return render(request,'shop/index.html',ctx)


def shop(request, store_id):
    ctx = {
        'shop':Shop.objects.get(id=store_id)

    }
    return render(request,'shop/shop.html',ctx)