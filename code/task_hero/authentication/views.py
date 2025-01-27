from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages



# Create your views here.


def sign_up(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Proceed to login.")
            return redirect("authentication:login")
    return render(request, "authentication/sign-up.html", {"form":form})


# def login(request):
#     form = UserCreationForm()
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             messages.success(request, "login successfully")
#             form.save()
#             return redirect("authentication:login")
#     return render(request, "authentication/log-in.html", {"form":form})



def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            messages.success(request, "Login successful.")
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect("home") 
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, "authentication/log-in.html", {"form": form})



