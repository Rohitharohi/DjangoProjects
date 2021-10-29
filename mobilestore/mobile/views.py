from django.shortcuts import render,redirect
from mobile import forms
from mobile.models import Mobile

# Create your views here.
def Add_mobile(request):
    if request.method=="GET":
        form=forms.Mobileform()
        contaxt={}
        contaxt["form"]=form
        return render(request,"add_mobile.html",contaxt)

    if request.method=="POST":
        form=forms.Mobileform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
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
            print("mobile saved")
            return redirect("mobilelist")
        else:
            return render(request,"add_mobile.html",{"form":form})

def mobile(request):
    return render(request,"mobile_home.html")

#
def list_mobile(request):
    mobiles=Mobile.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"mobile_list.html",context)

def remove_mobile(request,id):
    mobile=Mobile.objects.get(id=id)
    mobile.delete()
    return redirect("mobilelist")

def change_mobile(request,id):
    mobile=Mobile.objects.get(id=id)
    if request.method=="GET":
        # form=forms.Mobileform(initial={"mobile_name":mobile.mobile_name,"color":mobile.color,
        #     "ram":mobile.ram,"price":mobile.price,"availability":mobile.availability})
        form = forms.Mobileform(instance=mobile)
        context={}
        context["form"]=form
        return render(request,"edit_mobile.html",context)
    if request.method=="POST":
        form=forms.Mobileform(request.POST,instance=mobile)
        if form.is_valid():
            form.save()
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
            return redirect("mobilelist")

def mobile_details(request,id):
    mobile=Mobile.objects.get(id=id)
    context={}
    context["mobile"]=mobile
    return render(request,"mobile_details.html",context)
