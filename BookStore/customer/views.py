from django.shortcuts import render,redirect
from customer import forms
from django.contrib.auth import authenticate,login,logout
from Book.models import Book
from django.views.generic import TemplateView,ListView
from Book.models import Cart,Orders
from django.contrib import messages
from Book.decorators import signin_required
from django.utils.decorators import method_decorator
from django.db.models import Sum
from Book.filters import BookFilter




# Create your views here.
@method_decorator(signin_required,name="dispatch")
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


@method_decorator(signin_required,name="dispatch")
class Addtocart(TemplateView):
    model=Cart
    def get(self, request, *args, **kwargs):
        id=kwargs["id"]
        book=Book.objects.get(id=id)
        cart=Cart.objects.create(item=book,user=request.user)
        cart.save()
        messages.success(request,"item added to Cart")
        # print("item added to cart")
        return redirect("customerhome")


@method_decorator(signin_required,name="dispatch")
class Viewmycart(TemplateView):
    model=Cart
    template_name = "mycartitems.html"
    def get(self, request, *args, **kwagrs):
        context={}
        items=Cart.objects.filter(user=request.user,status="incart")
        context["items"]=items
        # total=Cart.objects.filter(user=request.user,status="incart").aggregate(Sum("item__price"))
        # print(total)
        # self.context["total"]=total["item__price__sum"]
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
@signin_required
def signout(request,*args,**kwargs):
    logout(request)
    return redirect("signin")


@method_decorator(signin_required,name="dispatch")
class Removeitemformcart(TemplateView):
    model=Cart
    def get(self, request, *args, **kwargs):
        id=kwargs["id"]
        cart=self.model.objects.get(id=id)
        cart.status="cancelled"
        cart.save()
        messages.success(request, "item has been removed")
        return redirect("customerhome")


@method_decorator(signin_required,name="dispatch")
class Ordercreate(TemplateView):
    model=Orders
    form_class=forms.Orderform
    template_name="ordercreate.html"
    context={}
    def get(self, request, *args, **kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,**kwargs):
        cart_id=kwargs["id"]
        cart_item=Cart.objects.get(id=cart_id)
        form=self.form_class(request.POST)
        if form.is_valid():
            address=form.cleaned_data["address"]
            user=request.user.username
            item=cart_item.item
            order=self.model.objects.create(
                item=item,
                user=user,
                addres=address


            )
            order.save()
            cart_item.status="orderplaced"
            cart_item.save()
            messages.success(request,"your order hasbeen placed")
            return redirect("customerhome")


@method_decorator(signin_required,name="dispatch")
class RemoveOrderedItem(TemplateView):
    model=Orders
    def get(self, request, *args, **kwargs):
        id=kwargs["id"]
        cart = self.model.objects.get(id=id)
        cart.status = "cancelled"
        cart.save()
        messages.success(request, "item has been removed")
        return redirect("customerhome")



# class Myorders():
#     model=Orders
#     template_name = "myorders.html"
    # def get(self, request, *args, **kwargs):
    #     context={}
    #     # books = Book.objects.all()
    #
    #     items = self.model.objects.filter(user=request.user,status="orderplaced")
    #
    #     context["items"] = items
    #     return render(request, self.template_name, context)
@method_decorator(signin_required,name="dispatch")
class Viewmyorder(ListView):
    model = Orders
    template_name = "myorders.html"
    context_object_name = "orders"

    def get_queryset(self):
        queryset=super().get_queryset()
        queryset=self.model.objects.filter(user=self.request.user)
        return queryset


class Bookfindview(TemplateView):
    template_name = "books.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        f=BookFilter(self.request.GET,queryset=Book.objects.all())
        context["filter"]=f
        return context
