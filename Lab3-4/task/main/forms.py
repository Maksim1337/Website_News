from .models import News
from django.forms import ModelForm, TextInput, Textarea


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ["title", "data", "img"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                 'label': '1',
                'placeholder': 'Введите название'
            }),
            "data": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            })
        }

