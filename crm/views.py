from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider


def first_page(request):
    slider_list = CmsSlider.objects.all()
    context = {
        'slider_list': slider_list,
    }
    return render(request, 'index.html', context)


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name=name, order_phone=phone)
    element.save()
    context = {
        'name': name,
        'phone': phone,
    }
    return render(request, 'thanks_page.html', context)

