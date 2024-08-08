from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

from account.forms import LoginUserForm, NewUserForm

def login(request):
    if request.user.is_authenticated and "next" in request.GET:
        return render(request, "account/login.html", {"error":"Unauthorized entry"})
    
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)  
                messages.add_message(request, messages.SUCCESS, "Login successfully")
                nextUrl = request.GET.get("next", None)
                if nextUrl is None:
                    return redirect("items")
                else:
                    return redirect(nextUrl)
            else:
                return render(request, "account/login.html", {"form": form})
        else:
            return render(request, "account/login.html", {"form": form})
    else:
        form = LoginUserForm()
        return render(request, "account/login.html", {"form": form})


def logout(request):
    auth_logout(request)  
    messages.add_message(request, messages.ERROR, "Logout :(")
    return redirect("items")


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(request, username=username, password=password)
            auth_login(request, user)  
            return redirect("items")
        else:
            return render(request, "account/register.html", {"form": form})
    else:
        form = NewUserForm()
        return render(request, "account/register.html", {"form": form})
