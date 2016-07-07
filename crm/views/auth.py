from django.contrib import auth
from django.shortcuts import redirect
from django.shortcuts import render


def login(request):
    if request.user.is_authenticated():
        return redirect('profile')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('profile')

    return render(request, 'auth/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')
