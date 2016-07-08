from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from crm.forms import AddUserForm, EditUserForm
from django.contrib.auth.models import User


@permission_required('user.is_superuser', login_url='login')
def user_list(request):
    users = User.objects.all()
    return render(request, 'user/user_list.html', {'users': users})


@permission_required('user.is_superuser', login_url='login')
def user_details(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user/user_details.html', {'user': user})


@permission_required('user.is_superuser', login_url='login')
def user_new(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_superuser = bool(request.POST.get('is_superuser'))
            user.save()
            return user_list(request)
    else:
        form = AddUserForm()
    return render(request, 'user/user_add.html', {'form': form})


@permission_required('user.is_superuser', login_url='login')
def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_superuser = bool(request.POST.get('is_superuser'))

            password = str(request.POST.get('new_password'))
            if password:
                user.set_password(password)

            user.save()
            return user_list(request)
    else:
        form = EditUserForm(instance=user)
    return render(request, 'user/user_edit.html', {'form': form})


@permission_required('user.is_superuser', login_url='login')
def user_delete(request, pk):
    User.objects.filter(pk=pk).delete()
    return user_list(request)
