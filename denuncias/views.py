from urllib import request
from django.shortcuts import render, redirect # type: ignore
from .forms import DenunciaForm
from django.contrib import messages # type: ignore

def registrar_denuncia(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Denúncia registrada com sucesso!')
            return redirect('registrar_denuncia')
    else:
        form = DenunciaForm()
    return render(request, 'denuncia/registrar_denuncia.html',{'form': form})
