from django import forms

from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content' : forms.Textarea(attrs={"class": "form-control", "rows": 10}),
            'category' : forms.Select(attrs={"class": "form-control"}),
        }
