from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from crm.forms import EditUserForm
from django.contrib.auth.models import User


def profile_view(request):
    if request.user.is_superuser:
        return render(request, 'crm/profile.html')
    return redirect('company_list')


def users_list(request):
    users = User.objects.all()
    return render(request, 'crm/users_list.html', {'users': users})


def user_details(request, pk):
    if request.user.is_superuser:
        user = get_object_or_404(User, pk=pk)
        return render(request, 'crm/user_details.html', {'user': user})
    return redirect('profile')


def user_new(request):
    if request.method == "POST":
        form = EditUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('user_details', pk=user.pk)
    else:
        form = EditUserForm()
    return render(request, 'crm/user_edit.html', {'form': form})


def user_edit(request, pk):
    if request.user.is_superuser:
        user = get_object_or_404(User, pk=pk)
        if request.method == "POST":
            form = EditUserForm(request.POST, instance=user)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                return redirect('user_details', pk=user.pk)
        else:
            form = EditUserForm(instance=user)
        return render(request, 'crm/user_edit.html', {'form': form})
