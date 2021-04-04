from django import forms
from authapp.models import ProjektUser
# from authapp.forms import ProjektEditForm
from projektapp.models import Projekt

# class ShopUserAdminEditForm(ShopUserEditForm):
#     class Meta:
#         model = ShopUser
#         fields = '__all__'

# class ProductCategoryEditForm(forms.ModelForm):
#     class Meta:
#         model = ProductCategory
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'
#             field.help_text = ''


class ProjektCreateForm(forms.ModelForm):
    class Meta:
        model = Projekt
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''



# class ProductEditForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'
#             field.help_text = ''



