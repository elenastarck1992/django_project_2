from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    """
    Класс для стилизации форм
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    """
    Класс для обработки GET и POST запросов со страницы product_form.html
    для создания, валидации и стилизации форм
    """

    forbidden_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')

    class Meta:
        model = Product
        exclude = ['date_of_change', 'date_of_creation', 'owner']

    def clean_product_name(self):
        """
        Функция валидации по имени товара
        """
        cleaned_data = self.cleaned_data.get('product_name')
        forbidden_words = self.forbidden_words

        if cleaned_data.lower().strip() in forbidden_words:
            raise forms.ValidationError('Название товара содержит запрещенные слова')

        return cleaned_data

    def clean_description(self):
        """
        Функция валидации по описанию товара
        """

        cleaned_data = self.cleaned_data.get('description')
        forbidden_words = self.forbidden_words

        if cleaned_data.lower().strip() in forbidden_words:
            raise forms.ValidationError('Описание товара содержит запрещенные слова')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    """
    Класс для обработки GET и POST запросов со страницы product_form.html
    для создания и стилизации форм
    """

    class Meta:
        model = Version
        fields = '__all__'

