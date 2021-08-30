from django import forms

from .models import Category


class BlogForm(forms.Form):
    title = forms.CharField(max_length=150,
                            label='Название',
                            widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label='Текст',
                              required=False,
                              widget=forms.Textarea(attrs={"class": "form-control","rows": 10,}),
                              )
    is_published = forms.BooleanField(label='Опубликовано?', required=False, initial=True)
    category = forms.ModelChoiceField(empty_label='Выберите категорию',
                                      queryset=Category.objects.all(),
                                      label='Категория',
                                      widget=forms.Select(attrs={"class": "form-control"})
                                      )
