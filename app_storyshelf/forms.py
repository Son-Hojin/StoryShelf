from django import forms
from app_storyshelf.models import Content
from django.utils.translation import gettext_lazy as _


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['book_name', "author", "content"]

        labels = {
            'book_name': _('책이름'),
            'author': _('작가'),
            'content': _('내용'),
        }
        widgets ={
            'book_name': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%; margin-bottom: 20px', 'placeholder': '책 이름을 입력하세요.', "autocomplete":"off"}
            ),
            'author': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%; margin-bottom: 20px', 'placeholder': '작가를 입력하세요.', "autocomplete":"off"}
            ),
            'content': forms.Textarea(
                attrs={'class': 'form-control','id':'scr', 'rows': "4", "style": "margin-bottom: 10px;", "autocomplete": "off"}
            )
        }