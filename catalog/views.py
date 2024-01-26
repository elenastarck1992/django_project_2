from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Contact, Category, Version


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


class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    Класс для обработки GET и POST запросов со страницы product_form.html
    для создания нового товара
    """
    # template_name = 'catalog/index.html'
    model = Product
    form_class = ProductForm
    extra_context = {'title': 'Магазин техники e-Shop'}
    success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """
    Класс для обработки GET и POST запросов со страницы product_form.html
    для редактирования товара
    """
    model = Product
    form_class = ProductForm
    extra_context = {'title': 'Магазин техники e-Shop'}
    success_url = reverse_lazy('catalog:index')


class ProductListView(LoginRequiredMixin, ListView):
    """
    Класс для обработки GET и POST запросов со страницы product_list.html
    для отображения страницы со списком товаров
    """
    template_name = 'catalog/index.html'
    model = Product
    extra_context = {'title': 'Магазин техники e-Shop'}

    def get_queryset(self):
        queryset = super().get_queryset()
        # queryset = queryset.filter(owner=self.owner)
        return queryset


class ProductDetailView(LoginRequiredMixin, DetailView):
    """
    Класс для обработки GET и POST запросов со страницы product_detail.html
    для отображения страницы отдельного товара
    """
    model = Product
    extra_context = {'title': 'Товары'}

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class VersionCreateView(LoginRequiredMixin, CreateView):
    """
    Класс для обработки GET и POST запросов со страницы product_form.html
    для создания нового товара
    """
    template_name = 'catalog/product_form.html'
    model = Version
    form_class = VersionForm
    extra_context = {'title': 'Магазин техники e-Shop'}
    success_url = reverse_lazy('catalog:index')

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
# def own_products(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(product_id=pk, owner=request.user)
#     }
#     return render(request, 'catalog/index.html', context)


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
