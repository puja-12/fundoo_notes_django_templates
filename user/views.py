import json
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from user.models import User

# Create your views here.




def index(request):
    return render(request, 'index.html')


def registration_view(request):
    """
    post method for registering a user
     """

    if request.method == "POST":
        print(request.POST)
        User.objects.create_user(username=request.POST["username"],
                                        password=request.POST["password"],
                                        email=request.POST["email"],
                                        first_name=request.POST["first_name"],
                                        last_name=request.POST["last_name"],
                                        phone_number=request.POST["phone_number"],
                                        location=request.POST["location"])

        messages.success(request, "Your account has been successfully created.")

        return redirect('login')

    return render(request, 'registration.html')


def login_view(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user:
            login(request, user)
            messages.success(request,"Successfully log in.")
            return redirect("profile")
        else:
            messages.error(request, 'invalid credentials.')
    return render(request, 'login.html')



def profile(request):
    first_name = ""
    if request.user.is_authenticated:
        first_name = request.user.first_name
    print(first_name)
    return render(request, 'profile.html', {"first_name": first_name})
