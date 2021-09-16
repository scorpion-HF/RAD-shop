from django import forms
from .models import CartItem, Order


class AddToCartForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs.update({
            'class': 'form-control-sm text-black',
            'name': "quantity",
            'min': "1",
            'style': "width: 100px;"
        })
        self.fields['quantity'].label = 'تعداد'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'postal_code', 'phone_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].widget.attrs.update({
            'class': 'form-control text-black',
            'name': "address",
            'rows': '4',
        })
        self.fields['postal_code'].widget.attrs.update({
            'class': 'form-control text-black',
            'name': "postal_code",
        })
        self.fields['phone_number'].widget.attrs.update({
            'class': 'form-control text-black',
            'name': "phone_number",
        })






