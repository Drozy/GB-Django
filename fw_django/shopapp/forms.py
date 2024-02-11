from django import forms

from shopapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'image']


# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 100}))
#     price = forms.DecimalField(max_digits=10, decimal_places=2)
#     stock = forms.IntegerField(min_value=0, default=0)
#     image = forms.ImageField()
