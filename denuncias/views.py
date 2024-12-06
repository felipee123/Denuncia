from django.shortcuts import render, redirect
from .forms import ReportForm, NonAnonymousReportForm
from django.shortcuts import get_object_or_404
from .models import Denuncia

def home(request):
    return render(request, 'home.html')

def search_report(request):
    if request.method == 'POST':
        token = request.POST.get('token')
        report = get_object_or_404(Denuncia, token=token)
        return render(request, 'report_detail.html', {'report': report})
    return render(request, 'search_report.html')

def anonymous_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.is_anonymous = True
            report.save()
            return render(request, 'report_success.html', {'token': report.token})
    else:
        form = ReportForm()
    return render(request, 'anonymous_report.html', {'form': form})

def non_anonymous_report(request):
    if request.method == 'POST':
        form = NonAnonymousReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.is_anonymous = False
            report.reporter_email = form.cleaned_data['email']
            report.save()
            return render(request, 'report_success.html', {'token': report.token})
    else:
        form = NonAnonymousReportForm()
    return render(request, 'non_anonymous_report.html', {'form': form})
