from django.shortcuts import render,redirect
from mobile import forms
from mobile.models import Mobile,Orders
from django.views.generic import CreateView,ListView,DetailView,DeleteView,UpdateView,TemplateView
from django.urls import reverse_lazy
from mobile.decorators import signin_required,admin_permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from mobile.filters import MobileFilter


# Create your views here.
@method_decorator(admin_permission_required,name="dispatch")
def Viewhomepage(request):
    return render(request,"page.html")

class Addmobile(CreateView):
    model = Mobile
    form_class = forms.Mobileform
    context_object_name = "form"
    template_name = "add_mobile.html"
    success_url = reverse_lazy("mobilelist")

# def Add_mobile(request):
#     if request.method=="GET":
#         form=forms.Mobileform()
#         contaxt={}
#         contaxt["form"]=form
#         return render(request,"add_mobile.html",contaxt)
#
#     if request.method=="POST":
#         form=forms.Mobileform(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()

            # print(form.cleaned_data)
            # mobile_name=form.cleaned_data["mobile_name"]
            # color=form.cleaned_data["color"]
            # ram=form.cleaned_data["ram"]
            #
            # price=form.cleaned_data["price"]
            # availability=form.cleaned_data["availability"]
            # print(mobile_name,color,ram,price,availability)
            # mobiles=Mobile.objects.create(mobile_name=mobile_name,color=color,ram=ram,price=price,availability=availability)
            # mobiles.save()

        #     print("mobile saved")
        #     return redirect("mobilelist")
        # else:
        #     return render(request,"add_mobile.html",{"form":form})

def mobile(request):
    return render(request,"mobile_home.html")


# class Listbook(ListView):
#     model=Mobile
#     template_name = "mobile_list.html"
#     context_object_name = "mobiles"
#     def get_queryset(self):
#
#         queryset = super().get_queryset()
#         queryset = self.model.objects.filter(user=self.request.user)
#         return queryset

@method_decorator(admin_permission_required,name="dispatch")
class Listmobile(ListView):
    model=Mobile
    context_object_name = "mobiles"
    template_name = "mobile_list.html"

# def list_mobile(request):
#     mobiles=Mobile.objects.all()
#     context={}
#     context["mobiles"]=mobiles
#     return render(request,"mobile_list.html",context)

@method_decorator(admin_permission_required,name="dispatch")
class Removemobile(DeleteView):
    model = Mobile
    template_name = "removebook.html"
    context_object_name = "mobile"
    success_url = reverse_lazy("mobilelist")
    pk_url_kwarg = "id"


# def remove_mobile(request,id):
#     mobile=Mobile.objects.get(id=id)
#     mobile.delete()
#     return redirect("mobilelist")

@method_decorator(admin_permission_required,name="dispatch")
class Changemobile(UpdateView):
    model = Mobile
    form_class = forms.Mobileform
    template_name = "edit_mobile.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("mobilelist")

# def change_mobile(request,id):
#     mobile=Mobile.objects.get(id=id)
#     if request.method=="GET":
#         # form=forms.Mobileform(initial={"mobile_name":mobile.mobile_name,"color":mobile.color,
#         #     "ram":mobile.ram,"price":mobile.price,"availability":mobile.availability})
#         form = forms.Mobileform(instance=mobile)
#         context={}
#         context["form"]=form
#         return render(request,"edit_mobile.html",context)
#     if request.method=="POST":
#         form=forms.Mobileform(request.POST,instance=mobile)
#         if form.is_valid():
#             form.save()

            # mobile_name=form.cleaned_data["mobile_name"]
            # color=form.cleaned_data["color"]
            # ram=form.cleaned_data["ram"]
            # price=form.cleaned_data["price"]
            # availability=form.cleaned_data["availability"]
            # mobile.mobile_name=mobile_name
            # mobile.color=color
            # mobile.ram=ram
            # mobile.price=price
            # mobile.availability=availability
            # mobile.save()

            # return redirect("mobilelist")

@method_decorator(admin_permission_required,name="dispatch")
class Mobiledetails(DetailView):
    model = Mobile
    pk_url_kwarg = "id"
    context_object_name = "mobile"
    template_name = "mobile_details.html"

# def mobile_details(request,id):
#     mobile=Mobile.objects.get(id=id)
#     context={}
#     context["mobile"]=mobile
#     return render(request,"mobile_details.html",context)

@method_decorator(admin_permission_required,name="dispatch")
class Vieworders(ListView):
    model=Orders
    template_name = "customer_orders.html"
    context_object_name = "orders"


    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        neworders=self.model.objects.filter(status="orderplaced")
        context["neworders"]=neworders
        d_orders=self.model.objects.filter(status="delivered")
        context["d_orders"]=d_orders

        context["neworders_count"]=neworders.count()
        context["d_orders_count"]=d_orders.count()
        return context


@method_decorator(admin_permission_required,name="dispatch")
class Viewmobiledetail(DetailView):
    model = Orders
    template_name = "ordered_mobiledetail.html"
    context_object_name = "mobile"
    pk_url_kwarg = "id"

class Adminlogin(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.adminloginform()
        context = {"form": form}
        return render(request, "login.html", context)

    def post(self, request):
        form = forms.adminloginform(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if (user):
                login(request, user)
                return redirect("customerhome")
        else:
            context = {"form": form}
            return render(request, "adminlogin.html", context)



@method_decorator(admin_permission_required,name="dispatch")
class OrderUpdateview(UpdateView):
    model = Orders
    form_class = forms.Updateform
    template_name = "updateorder.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("customerorders")


class MobileSearch(TemplateView):
    template_name = "mobiles.html"
    def get(self,*args,**kwargs):
        context=super().get_context_data(**kwargs)
        f=MobileFilter(self.request.GET,queryset=Mobile.objects.all())
        context["filter"]=f
        return context

