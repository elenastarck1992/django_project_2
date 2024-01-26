from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog


class BlogCreateView(LoginRequiredMixin, CreateView):
    """
    Класс для обработки GET и POST запросов со страницы blog_form.html
    для создания блоговой записи
    """
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    """
    Класс для обработки GET и POST запросов со страницы blog_form.html
    для редактирования отдельной блоговой записи
    """
    model = Blog
    fields = ('title', 'slug', 'content', 'preview', 'create_date', 'is_published',)

    # success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogListView(ListView):
    """
    Класс для обработки GET запросов со страницы blog_list.html
    для отображения страницы со списком блоговых записей
    """
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)

        return queryset


class BlogDetailView(DetailView):
    """
    Класс для обработки GET запросов со страницы blog_detail.html
    для отображения отдельной блоговой записи со счетчиком просмотров
    """
    model = Blog
    success_url = reverse_lazy('blog:list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()

        return self.object


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    """
    Класс для обработки GET и POST запросов со страницы blog_detail.html
    для удаления отдельной блоговой записи
    """
    model = Blog
    success_url = reverse_lazy('blog:list')
