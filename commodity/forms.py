from django import forms
from . models import OrderModel

# class Contact_Form(forms.ModelForm):
#     class Meta:
#         model = contactModel
#         fields =  ['FullName','Email','Subject','Message']


class Order_Form(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields =  ['laptop']
        # 'accessories','desktop','motherBoards','mobile',

# class Contact_Form(forms.ModelForm):
#     class Meta:
#         model = contactModel
#         fields =  ['FullName','Email','Subject','Message']

# class Payment_Form(forms.ModelForm):
#     class Meta:
#         model = orderModel
#         fields =  []

