from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from catalog.models import Product, Contact, Category


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


class ProductListView(ListView):
    template_name = 'catalog/index.html'
    model = Product
    extra_context = {'title': 'Магазин техники e-Shop'}

class ProductDetailView(DetailView):
    model = Product
    extra_context = {'title': 'Товары'}

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

# def index_home(request):
#     """
#     Функция для обработки GET запросов со страницы index_home.html
#     """
#     latest_products = Product.objects.all().order_by('-id')
#     print(latest_products[:5])
#     return render(request, 'catalog/index_home.html'
#                            '')

# def index(request):
#     """
#     Функция для обработки GET запросов со страницы отображения продуктов product_list.html
#     """
#     context = {
#         'object_list': Product.objects.all(),
#         'title': 'Магазин техники e-Shop'
#     }
#     return render(request, 'catalog/blog_list.html', context
#                   )

# class ProductCreateView(CreateView):
#     model = Product
#     fields = ('product_name', 'description', 'image', 'category', 'price', 'date_of_creation',)
#     success_url = reverse_lazy('catalog:index')

# def get_queryset(self):
#     queryset = super().get_queryset()
#     queryset = queryset.filter()

# def product(request, pk):
#     """
#     Функция для обработки GET запросов со страницы отображения продуктов product_list.html
#     """
#     context = {
#         'object_list': Product.objects.get(pk=pk),
#         'title': 'Товары'
#     }
#     return render(request, 'catalog/product_list.html', context)
