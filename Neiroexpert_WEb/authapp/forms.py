from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from authapp.models import ProjektUser
from django.core import validators


class ProjektUserLoginForm (AuthenticationForm):

    class Meta:
        model = ProjektUser 
        fields = ('username', 'password')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] ='form-control'

class ProjektUserRegisterForm(UserCreationForm):
    class Meta:
        model = ProjektUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'age', 'avatar')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] ='form-control'
            # field.help_text = ''
        
    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return data

class ProjektUserEditForm(UserChangeForm):
    
    class Meta:
        model = ProjektUser
        fields = ('username', 'first_name', 'email', 'age', 'avatar', 'password')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return data