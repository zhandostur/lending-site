from django.shortcuts import render
from .models import Order
def first_page(request):
    object_list = Order.objects.all()
    return render(request, 'index.html', {'object_list': object_list})


def thanks_page(request):
    # if request.method == 'POST':
    #     name = request.GET['name']
    #     phone = request.GET['phone']
    #     if name.isvalid() and phone.isvalid:

    context = {
        'name': name,
        'phone': phone,
    }
    return render(request, 'thanks_page.html', context)

#
# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Вы успешно зарегестрированы!')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegistrationForm()
#     context = {'form': form}
#     return render(request, 'users/registration.html', context)
