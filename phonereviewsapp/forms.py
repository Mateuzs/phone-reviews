from django.forms import ModelForm
from phonereviewsapp.models import Phone, Store


class PhoneForm(ModelForm):

    class Meta:
        model = Phone
        exclude = ('user', 'date',)


class StoreForm(ModelForm):

    class Meta:
        model = Store
        exclude = ('user', 'date', 'phone',)
