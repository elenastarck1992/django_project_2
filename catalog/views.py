from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
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


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Класс для обработки GET и POST запросов со страницы product_form.html
    для редактирования товара
    """
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_published_status'
    extra_context = {'title': 'Магазин техники e-Shop'}
    success_url = reverse_lazy('catalog:index')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object


class ProductListView(ListView):
    """
    Класс для обработки GET и POST запросов со страницы product_list.html
    для отображения страницы со списком товаров
    """
    template_name = 'catalog/index.html'
    model = Product
    extra_context = {'title': 'Магазин техники e-Shop'}

    def get_queryset(self):
        queryset = super().get_queryset()
        # queryset = super().get_queryset().filter(
        #     category_id=self.kwargs.get('pk'),
        #     )
        if not self.request.user.is_staff and self.request.user.is_authenticated:
            queryset = queryset.filter(owner=self.request.user)
        return queryset
    #
    def get_form_class(self):
        if self.request.user == self.object.user:
            return ProductForm
        elif self.request.user.has_perm('catalog.set_published'):
            return ModeratorProductForm
        else:
            raise Http404('Вы не имеете права на редактирование чужих товаров')

    # def get_context_data(self, *args, **kwargs):
    #     context_data = super().get_context_data(*args, **kwargs)
    #     category_item = Category.objects.get(pk=self.kwargs.get('pk'))
    #     context_data['category_pk'] = category_item.pk
    #     context_data['title'] = f'Магазин техники e-Shop {category_item.category_name}'
    #     return context_data


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


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')


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
