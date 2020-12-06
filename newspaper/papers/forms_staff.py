from django import forms
from .models import *
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
    publish_date = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y', )
    )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ReporterForm(forms.ModelForm):
    class Meta:
        model = Reporter
        fields = '__all__'
