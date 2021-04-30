from django import forms
from .models import MyUser


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['name', 'email', 'password']
        # fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'emailid'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'passwordid'}),
        }
