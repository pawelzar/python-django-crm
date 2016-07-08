from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from crm.models import Company
from crm.forms import CompanyForm


@login_required(login_url='login')
def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company/company_list.html',
                  {'companies': companies})


@login_required(login_url='login')
def company_details(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'company/company_details.html',
                  {'company': company})


@permission_required('user.is_superuser', login_url='login')
def company_new(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.save()
            return redirect('company_details', pk=company.pk)
    else:
        form = CompanyForm()
    return render(request, 'company/company_add.html', {'form': form})


@permission_required('user.is_superuser', login_url='login')
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
    return render(request, 'company/company_edit.html', {'form': form})


@permission_required('user.is_superuser', login_url='login')
def company_delete(request, pk):
    Company.objects.filter(pk=pk).delete()
    return company_list(request)
