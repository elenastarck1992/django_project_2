from django.shortcuts import render


def index_home(request):
    """
    Функция для обработки GET запросов со страницы index_home.html
    """
    return render(request, 'catalog/index_home.html'
                           '')


def index_contacts(request):
    """
    Функция для обработки GET и POST запросов со страницы index_contacts.html
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{email}: {message}')
    return render(request, 'catalog/index_contacts.html')
