from .models import News
from django.forms import ModelForm, TextInput


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ["title", "data", "time"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "data": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'

            }),
            "time": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите время'

            })
        }

