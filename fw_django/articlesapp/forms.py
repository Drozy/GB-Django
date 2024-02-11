from django import forms

from .models import AuthorModel, ArticleModel


class AuthorForm(forms.ModelForm):
    class Meta:
        model = AuthorModel
        fields = ['firstname', 'lastname', 'email', 'bio', 'dob']


# class AuthorForm(forms.Form):
#     firstname = forms.CharField(max_length=100)
#     lastname = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     bio = forms.CharField(widget=forms.Textarea)
#     dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))


class ArticleForm(forms.ModelForm):
    class Meta:
        model = ArticleModel
        fields = ['title', 'content', 'author', 'category', 'publication_flag']
