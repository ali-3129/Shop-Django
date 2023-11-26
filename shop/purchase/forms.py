from django import forms

from purchase.models import Purchase


class IForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('quantity',)
