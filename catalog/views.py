from django.shortcuts import render

from catalog.models import Product, Contact


def index_home(request):
    """
    Функция для обработки GET запросов со страницы index_home.html
    """
    latest_products = Product.objects.all().order_by('-id')
    print(latest_products[:5])
    return render(request, 'catalog/index_home.html'
                           '')


def index_contacts(request):
    """
    Функция для обработки GET и POST запросов со страницы index_contacts.html
    """
    contacts = Contact.objects.all()
    print(contacts)
    if request.method == 'POST':
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{email} {phone}: {message}')
    return render(request, 'catalog/index_contacts.html', {'contact': contacts})
