from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def home_page(request):
    return render(request, "pages/home.html")

def about_page(request):
    return render(request, "pages/about.html")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'pages/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'pages/profile.html')