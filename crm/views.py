from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Company
from .forms import CompanyForm
from django.contrib.auth.models import User


def profile_view(request):
    return render(request, 'crm/profile.html')


def users_list(request):
    users = User.objects.all()
    return render(request, 'crm/users_list.html', {'users': users})


def company_list(request):
    companys = Company.objects.all()
    return render(request, 'crm/company_list.html', {'companys': companys})


def company_details(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'crm/company_details.html', {'company': company})


def company_new(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.save()
            return redirect('company_details', pk=company.pk)
    else:
        form = CompanyForm()
    return render(request, 'crm/company_edit.html', {'form': form})


def company_edit(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            company = form.save(commit=False)
            company.save()
            return redirect('company_details', pk=company.pk)
    else:
        form = CompanyForm(instance=company)
    return render(request, 'crm/company_edit.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('../')
