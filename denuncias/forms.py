from django import forms
from .models import Denuncia

class ReportForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = ['title', 'description', 'category']

class NonAnonymousReportForm(forms.ModelForm):
    email = forms.EmailField(required=True)  # Adicionando campo personalizado

    class Meta:
        model = Denuncia
        fields = ['title', 'description', 'category']

