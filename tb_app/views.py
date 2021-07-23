from django.forms import fields
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home_page(request):
    return render(request, "home.html")

def price(request):
    return render(request, "prices.html")

def doc(request):
    return render(request, "doc.html")

def faq(request):
    return render(request, "faq.html")

def affiliate(request):
    return render(request, "affiliate.html")

def login_page(request):
    if request.user.is_authenticated:
        return redirect('tb_app:dashboard')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('tb_app:dashboard')

        context = {}
        return render(request, 'login.html', context)

def logout_page(request):
    logout(request)
    return redirect('tb_app:login')

def resetpassword(request):
    return render(request, 'accounts/password_reset.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('tb_app:dashboard')
    else:
        if request.method == "POST":
            form = UserRegisterForm(request.POST)

            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account Created for {username}')
                return redirect('tb_app:login')
            else:
                for field in form:
                    messages.error(request, f'{field.errors}')
                return redirect('tb_app:register')
        else:
            form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})

@login_required(login_url='tb_app:login')
def dashboard(request):
    return render(request, 'dashboard.html')
