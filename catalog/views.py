from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, ModeratorProductForm
from catalog.models import Product, Contact, Category, Version
from users.forms import ModeratorProductForm


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

    def get_form_class(self):
        if self.request.user == self.object.owner:
            return ProductForm
        elif self.request.user.groups.filter(name='moderator'):
            return ModeratorProductForm
        else:
            raise Http404('Вы не являетесь владельцем данного товара')


class ProductListView(ListView):
    """
    Класс для обработки GET и POST запросов со страницы product_list.html
    для отображения страницы со списком товаров
    """
    # template_name = 'catalog/index.html'
    model = Product
    extra_context = {'title': 'Магазин техники e-Shop'}


class ProductDetailView(DetailView):
    """
    Класс для обработки GET и POST запросов со страницы product_detail.html
    для отображения страницы отдельного товара
    """
    model = Product
    extra_context = {'title': 'Товары'}

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')

    def get_object(self, queryset=None, *args, **kwargs):
        object_data = super().get_object(*args, **kwargs)
        if self.request.user == object_data.owner:
            return object_data
        else:
            raise Http404('Вы не являетесь владельцем данного товара')


class VersionCreateView(LoginRequiredMixin, CreateView):
    """
    Класс для обработки GET и POST запросов со страницы product_form.html
    для создания нового товара
    """
    template_name = 'catalog/product_form.html'
    model = Version
    form_class = VersionForm
    permission_required = 'catalog.add_version'
    extra_context = {'title': 'Магазин техники e-Shop'}
    success_url = reverse_lazy('catalog:index')
