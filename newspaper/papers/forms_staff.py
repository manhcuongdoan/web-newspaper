from django import forms
from .models import *

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
    

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ReporterForm(forms.ModelForm):
    class Meta:
        model = Reporter
        fields = '__all__'
