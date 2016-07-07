from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from crm.forms import AddUserForm, EditUserForm
from django.contrib.auth.models import User


def profile_view(request):
    if request.user.is_superuser:
        return render(request, 'admin/choice.html')
    return redirect('company_list')


def user_list(request):
    users = User.objects.all()
    return render(request, 'user/user_list.html', {'users': users})


def user_details(request, pk):
    if request.user.is_superuser:
        user = get_object_or_404(User, pk=pk)
        return render(request, 'user/user_details.html', {'user': user})
    return redirect('profile')


def user_new(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return user_list(request)
    else:
        form = AddUserForm()
    return render(request, 'user/user_add.html', {'form': form})


def user_edit(request, pk):
    if request.user.is_superuser:
        user = get_object_or_404(User, pk=pk)
        if request.method == "POST":
            form = EditUserForm(request.POST, instance=user)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                return redirect('user_list')
        else:
            form = EditUserForm(instance=user)
        return render(request, 'user/user_edit.html', {'form': form})


def user_delete(request, pk):
    if request.user.is_superuser:
        User.objects.filter(pk=pk).delete()
    return user_list(request)
