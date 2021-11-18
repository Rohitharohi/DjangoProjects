from django.shortcuts import render, redirect
from customer import forms
from django.contrib.auth import authenticate, login, logout
from mobile.models import Mobile, Cart, Orders,User
from django.views.generic import TemplateView,ListView,CreateView,DetailView,DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from mobile.decorators import signin_required
from django.utils.decorators import method_decorator
from django.db.models import Sum
from  mobile.filters import MobileFilter

# Create your views here.

# class Customerhome(ListView):
#     model = Mobile
#     template_name = "home.html"
#     context_object_name = "mobiles"
@method_decorator(signin_required,name="dispatch")
class Customerhome(TemplateView):
    def get(self, request, *args, **kwargs):
        mobiles = Mobile.objects.all()
        context = {"mobiles": mobiles}
        return render(request, "home.html", context)


# def customer_home(request):
# mobiles=Mobile.objects.all()
# context={"mobiles":mobiles}
# return render(request,"home.html",context)


# class Signup(CreateView):
#     model = User
#     template_name = "user_registration.html"
#     form_class = forms.Userregistrationform
#     success_url = reverse_lazy("signin")


class Signup(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.Userregistrationform()
        context = {"form": form}
        return render(request, "user_registration.html", context)

    def post(self, request):
        form = forms.Userregistrationform(request.POST)
        if form.is_valid():
            form.save()
            # return render(request,"login.html")
            return redirect("signin")
        else:
            context = {"form": form}
            return render(request, "user_registration.html", context)

    # def sign_up(request):


#     form=forms.Userregistrationform()
#     context={"form":form}
#     if request.method=="POST":
#         form=forms.Userregistrationform(request.POST)
#         if form.is_valid():
#             form.save()
#             # return render(request,"login.html")
#             return redirect("signin")
#         else:
#             context["form"]=form
#             return render(request, "user_registration.html", context)

# return render(request,"user_registration.html",context)
#
# class Signin(CreateView):
#     model = Mobile
#     form_class = forms.Loginform
#     template_name = "login.html"
#     success_url = reverse_lazy("customerhome")



class Signin(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.Loginform()
        context = {"form": form}
        return render(request, "login.html", context)

    def post(self, request):
        form = forms.Loginform(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if (user):
                login(request, user)
                return redirect("customerhome")
        else:
            context = {"form": form}
            return render(request, "login.html", context)

    # def signin(request):


#     form=forms.Loginform()
#     context={"form":form}
#     if request.method=="POST":
#         form=forms.Loginform(request.POST)
#         if form.is_valid():
#             username=form.cleaned_data["username"]
#             password=form.cleaned_data["password"]
#             user=authenticate(request,username=username,password=password)
#             if(user):
#                 login(request,user)
#                 return redirect("customerhome")
#             else:
#                 return render(request, "login.html", context)

# return render(request,"login.html",context)
# def signin(request):
#
#     form=forms.Loginform()
#     context={"form":form}
#
#
#     if request.method=="POST":
#         form=forms.Loginform(request.POST)
#         if form.is_valid():
#             username=form.cleaned_data["username"]
#             password=form.cleaned_data["password"]
#             user=authenticate(request,username=username,password=password)
#             if user:
#                 login(request,user)
#                 return redirect("customerhome")
#             else:
#                 return render(request,"login.html",{"form":form})
#
#
#     return render(request,"login.html",context)


def signout(request):
    logout(request)
    return redirect("signin")

# class Addtocart(CreateView):
#     model=Cart
#     pk_url_kwarg = "id"
#     success_url = reverse_lazy("customerhome")


@method_decorator(signin_required,name="dispatch")
class Addtocart(TemplateView):
    model = Cart

    def get(self, request, *args, **kwargs):
        id = kwargs["id"]
        mobile = Mobile.objects.get(id=id)
#
        cart = Cart.objects.create(item=mobile, user=request.user)
        cart.save()
        print("added to cart")
        messages.success(request, "item added to your Cart")
        return redirect("customerhome")


@method_decorator(signin_required,name="dispatch")
class Viewmycart(TemplateView):
    model = Cart
    template_name = "viewmycart.html"
    # context_object_name = "items"
    context={}
    def get(self, request, *args, **kwargs):
        cart=self.model.objects.filter(user=request.user,status="incart")
        self.context["items"]=cart
        total=Cart.objects.filter(user=request.user,status="incart").aggregate(Sum("item__price"))
        self.context["total"]=total['item__price__sum']
        # cartitem=Cart.objects.filter(user=request.user,status="incart").aggregate(Sum("item__mobile_name"))
        # self.context["cartitem"]=cartitem['item__mobile_name__sum']

        return render(request,self.template_name,self.context)



# class Viewmycart(TemplateView):
#     model = Cart
#     template_name = "viewmycart.html"
#
#     def get(self, request, *args, **kwargs):
#         context = {}
#         items = Cart.objects.filter(user=request.user, status="incart")
#         context["items"] = items
#         return render(request, self.template_name, context)


@method_decorator(signin_required,name="dispatch")
class RemoveItem(TemplateView):
    model = Cart

    def get(self, request, *args, **kwargs):
        id = kwargs["id"]
        cart = self.model.objects.get(id=id)
        cart.status = "cancelled"
        cart.save()
        messages.success(request, "item hasbeen cancelled")
        return redirect("customerhome")

# class Ordercreate(CreateView):
#     model=Orders
#     template_name = "ordercreate.html"
#     form_class = forms.Orderform
#     success_url = reverse_lazy("customerhome")
#     pk_url_kwarg = "id"



@method_decorator(signin_required,name="dispatch")
class Ordercreate(TemplateView):
    model = Orders
    form_class = forms.Orderform
    template_name = "ordercreate.html"
    context = {}

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, **kwargs):
        cart_id = kwargs["id"]
        cart_item = Cart.objects.get(id=cart_id)
        form = self.form_class(request.POST)
        if form.is_valid():
            address = form.cleaned_data["address"]
            item = cart_item.item
            user = request.user.username
            order = self.model.objects.create(
                item=item,
                user=user,
                address=address

            )
            order.save()
        cart_item.status = "orderplaced"
        cart_item.save()
        messages.success(request, "your item hasbeen placed")
        return redirect("customerhome")

@method_decorator(signin_required,name="dispatch")
class Viewmyorders(ListView):
    model=Orders
    template_name = "myorders.html"
    context_object_name = "orders"



    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.model.objects.filter(user=self.request.user)
        return queryset



# class Myorders(TemplateView):
#     model = Orders
#     template_name = "myorders.html"
#     context = {}
#
#     def get(self, request, *args, **kwargs):
#         items = self.model.objects.filter(user=request.user, status="orderplaced")
#         self.context["items"] = items
#         return render(request, self.template_name, self.context)


@method_decorator(signin_required,name="dispatch")
class RemoveOrdereditem(TemplateView):
    model = Orders

    def get(self, request, *args, **kwargs):
        id = kwargs["id"]
        cart = self.model.objects.get(id=id)
        cart.status = "cancelled"
        cart.save()
        messages.success(request, "item removed")
        return redirect("customerhome")


class Mobilefindview(TemplateView):
    template_name = "mobiles.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        f=MobileFilter(self.request.GET,queryset=Mobile.objects.all())
        context["filter"]=f
        return context

# class Mobilessearchview(TemplateView):
#     template_name = "mobile.html"
#     def get(self,*args,**kwargs):
#         context=super().get_context_data(**kwargs)
#         f=MobileFilter(self.request.GET,queryset=Mobile.objects.all())
#         context["filter"]=f
#         return context