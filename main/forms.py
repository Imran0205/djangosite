from .models import advices
from django.forms import ModelForm, TextInput, Textarea

class adviceslol(ModelForm):
    class Meta:
        model = advices
        fields = ['Name', 'Advice']
        widgets = {
            'Name': TextInput(attrs={
                'class': 'hh',
                'placeholder': 'Имя',
                'maxlength': '15',
                'id': 'son',
            }),
            'Advice': Textarea(attrs={
                'class': 'hh',
                'placeholder': 'Совет',
                'maxlength': '300',
                'id': 'jon',
            })
        }