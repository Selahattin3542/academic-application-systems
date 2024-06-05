from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


# Create your views here.

def register1(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save()
        login(request, newUser)
        messages.info(request, "Başarıyla Kayıt Oldunuz...")

        return redirect("index")
        return render(request, "register1.html",  context)
    context = {
        "form": form
    }
    return render(request, "register1.html", context)


def loginUser1(request):
    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Kullanıcı Adı veya Parola Hatalı")
            return render(request, "login1.html", context)

        messages.success(request, "Başarıyla Giriş Yaptınız")
        login(request, user)
        return redirect("index")
    return render(request, "login1.html", context)


def logoutUser1(request):
    logout(request)
    messages.success(request, "Başarıyla Çıkış Yaptınız")
    return redirect("index")

