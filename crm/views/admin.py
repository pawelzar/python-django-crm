from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect


def choice_view(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'admin/choice.html')
        return redirect('company_list')
    return redirect('login')
