from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from crm.models import Company
from crm.forms import CompanyForm


def company_list(request):
    companies = Company.objects.all()
    return render(request, 'crm/company_list.html', {'companies': companies})


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
