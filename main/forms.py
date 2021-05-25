from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.db.models import fields
from django.utils.translation import ugettext as _
from main.choices import purchase, dispatch, gender_choices
from main.models import Purchase, Store, Item, Outlet, Supplier, User,Supplier
from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'gender', 'store']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['email', 'password']


class StoreModelForm(BSModalModelForm):
    class Meta:
        model = Store
        exclude = ['date_modified', 'date_added']


class SupplierModelForm(BSModalModelForm):
    class Meta:
        model = Supplier
        fields = ['email', 'name', 'address']


class OutletModelForm(BSModalModelForm):
    class Meta:
        model = Outlet
        exclude = ['date_modified', 'date_added']


class UserModelForm(BSModalModelForm):
    class Meta:
        model = User
        exclude = ['date_joined', 'is_active', 'is_staff']


class ItemModelForm(BSModalModelForm):
    class Meta:
        model = Item
        exclude = ['date_modified', 'date_added']


class SignForm(UserCreationForm):

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'aria-describedby': 'emailHelp',
                   'type': 'email'
                   }))
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'text',
                                      'name': 'first_name'
                                      }))

    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'text',
                                      'name': 'last_name'
                                      }))
    gender = forms.ChoiceField(choices=gender_choices,
                               label="Gender",
                               initial='Q',
                               widget=forms.Select(
                                   attrs={'class': 'form-control',
                                          }), required=True)
    store = forms.ModelChoiceField(
        queryset=Store.objects.all(), widget=forms.Select(
            attrs={'class': 'form-control'}), label="Store")

    password = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Password',
                                          'type': 'password',
                                          'name': 'password'
                                          }))
    rpassword = forms.CharField(
        label='Repeat Password',
        max_length=30,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Password',
                                          'type': 'password',
                                          'name': 'password'
                                          }))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password', '')
        repeat_password = cleaned_data.get('rpassword', '')
        if password == repeat_password:
            if len(repeat_password) < 8:
                raise forms.ValidationError('password is too short')
            else:
                raise forms.ValidationError('passwords do not match')


class PurchaseForm(forms.Form):

    barcode = forms.CharField(
        max_length=12,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'text',
                                      'name': 'first_name'
                                      }))
    quantity = forms.CharField(
        max_length=12,
        label="Quantity",
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'name': 'quantity'
                                        }))
    store = forms.ModelChoiceField(
        queryset=Store.objects.all(), widget=forms.Select(
            attrs={'class': 'form-control'}), label="Store")
    outlet = forms.ModelChoiceField(
        queryset=Outlet.objects.all(), widget=forms.Select(
            attrs={'class': 'form-control'}), label="Outlet")
    transaction_type = forms.ChoiceField(choices=purchase,
                                         label="Transaction",
                                         initial='decrease',
                                         widget=forms.Select(
                                             attrs={'class': 'form-control',
                                                    }), required=True)


class DispatchForm(forms.Form):

    barcode = forms.CharField(
        max_length=12,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'text',
                                      'name': 'first_name'
                                      }))
    quantity = forms.CharField(
        max_length=12,
        label="Quantity",
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'name': 'quantity'
                                        }))
    store = forms.ModelChoiceField(
        queryset=Store.objects.all(), widget=forms.Select(
            attrs={'class': 'form-control'}), label="Store")
    outlet = forms.ModelChoiceField(
        queryset=Outlet.objects.all(), widget=forms.Select(
            attrs={'class': 'form-control'}), label="Outlet")
    transaction_type = forms.ChoiceField(choices=dispatch,
                                         label="Transaction",
                                         initial='decrease',
                                         widget=forms.Select(
                                             attrs={'class': 'form-control',
                                                    }), required=True)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password', '')
        repeat_password = cleaned_data.get('rpassword', '')
        if password == repeat_password:
            if len(repeat_password) < 8:
                raise forms.ValidationError('password is too short')
            else:
                raise forms.ValidationError('passwords do not match')
