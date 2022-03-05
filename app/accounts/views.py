from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
from accounts.forms import RegistrationForm, LoginForm


def registration_view(request):
    form = RegistrationForm(request.POST or None, request.FILES or None)  # gdyby był 1 raz to none,

    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()

            # if form.cleaned_data['is_instructor'] is True:

        return redirect('accounts:login')

    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    form = LoginForm(request, request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(email=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')

    return render(request, 'accounts/login.html', {'form': form})