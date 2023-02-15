from django.shortcuts import render
from .models import Order
from .forms import OrderForm
def first_page(request):
    object_list = Order.objects.all()
    form = OrderForm()
    context = {
        'object_list': object_list,
        'form': form
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

