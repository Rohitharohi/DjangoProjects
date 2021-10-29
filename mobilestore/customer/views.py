from django.shortcuts import render,redirect
from customer import forms
from django.contrib.auth import authenticate,login,logout
from mobile.models import Mobile
# Create your views here.


def customer_home(request):
    mobiles=Mobile.objects.all()
    context={"mobiles":mobiles}
    return render(request,"home.html",context)



def sign_up(request):
    form=forms.Userregistrationform()
    context={"form":form}
    if request.method=="POST":
        form=forms.Userregistrationform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"login.html")
        else:
            context["form"]=form
            return render(request, "user_registration.html", context)

    return render(request,"user_registration.html",context)

def signin(request):
    form=forms.Loginform()

    if request.method=="POST":
        form=forms.Loginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("customerhome")
            else:
                return render(request,"login.html",{"form":form})


    return render(request,"login.html",{"form":form})


def signout(request):
    logout(request)
    return redirect("signin")
