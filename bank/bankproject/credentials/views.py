from django.contrib import messages, auth
from django.contrib.auth import authenticate , login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

from bankapp.models import Account


# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('credentials:register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
            print("user created")
            messages.info(request, "User Created")
        else:
            print("Password not matching")
            messages.info(request, "Password Not Matching")
            return redirect('credentials:register')
        return render(request,"login.html")
    return render(request,'register.html')


def user_login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            user = request.user
            user_id = user.id
            application = Account.objects.filter(user_id=user_id)
            context = {
                'application_list': application
            }

            return render(request, "landing.html", {'username': username,'application_list':application})
        else:
            messages.info(request, "Invalid Entry")
            return redirect('credentials:user_login')

    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    print("Logout Successfull")
    return redirect('/')


