from django import forms # type: ignore
from .models import Denuncia

class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = ['tipo_reporte', 'nome', 'email', 'descricao', 'arquivo_anexo']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 5}),
        }