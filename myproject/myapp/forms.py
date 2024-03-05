from django import forms
#from django.core.validators import MinLengthValidator, MaxLengthValidator

class InvocationForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Имя'}))
    second_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Фамилия'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Отчество'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Адресс'}))
    personal_account = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Личный счёт'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Обращение'}))