from django.shortcuts import render,redirect
from customer import forms
from django.contrib.auth import authenticate,login,logout
from Book.models import Book
from django.views.generic import TemplateView
from Book.models import Cart




# Create your views here.

class CustomerHome(TemplateView):
    def get(self,request,*args,**kwargs):
        books = Book.objects.all()
        context = {"books": books}
        return render(request, "home.html", context)


# class Customer_home(TemplateView):
#
#     books=Book.objects.all()
#     context={"books":books}
#     return render(request, "home.html",context)

class Signupview(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.Userregistrationform()
        context = {}
        context ["form"] = form
        return render(request, "user_registration.html", context)
    def post(self,request):
        form = forms.Userregistrationform(request.POST)
        if form.is_valid():
            form.save()
            print("user hasbeen created")
            return redirect("signin")

class Addtocart(TemplateView):
    model=Cart
    def get(self, request, *args, **kwargs):
        id=kwargs["id"]
        book=Book.objects.get(id=id)
        cart=Cart.objects.create(item=book,user=request.user)
        cart.save()
        print("item added to cart")
        return redirect("customerhome")

class Viewmycart(TemplateView):
    model=Cart
    template_name = "mycartitems.html"
    def get(self, request, *args, **kwagrs):
        context={}
        items=Cart.objects.filter(user=request.user)
        context["items"]=items
        return render(request,self.template_name,context)


# def sign_up(request):
#     form = forms.Userregistrationform()
#     context = {"form": form}
#     if request.method == "POST":
        # form = forms.Userregistrationform(request.POST)
        # if form.is_valid():
        #     form.save()
        #     print("user hasbeen created")
        #     return redirect("signin")
        # else:
        #     context["form"]=form
        #     return render(request, "user_registration.html", context)


    # return render(request, "user_registration.html", context)


class Signinview(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.Loginform()
        return render(request, "login.html", {"form": form})

    def post(self,request):
        form=forms.Loginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            print(user)
            if user:
                login(request,user)
                return redirect("customerhome")
        # else:
        #     return render(request,"login.html",{"form":form})


    # return render(request,"login.html",{"form":form})

def signout(request):
    logout(request)
    return redirect("signin")