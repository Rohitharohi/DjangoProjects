from django.shortcuts import render,HttpResponse,redirect
from centerhead.forms import courseform,batchform,Registrationform,Loginform


# Create your views here.
def home(request):
    return render(request,"centerhead_home.html")

def add_course(request):
    if request.method=="GET":
        form=courseform()
        contaxt={}
        contaxt["form"]=form
        return render(request,"add_course.html",contaxt)
    if request.method=="POST":
        form=courseform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            coursename=form.cleaned_data["c_name"]
            print(coursename)
            return render(request,"add_course.html")




def add_batches(request):
    if request.method=="GET":
        form=batchform()
        contaxt={}
        contaxt["form"]=form
        return render(request, "add_batch.html",contaxt)

    if request.method=="POST":
        form=batchform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            coursename=form.cleaned_data["c_name"]
            batchname=form.cleaned_data["b_name"]

            print(coursename,batchname)
            return redirect("batch")



def add_faculty(request):
    if request.method=="POST":
        userss=request.POST.get("usr")
        print(userss)
        addd=request.POST.get("add")
        print(addd)
        return render(request, "facultyy.html")

    return render(request,"facultyy.html")

def view_timesheet(request):
    timesheets = [
        {"user": "user1", "topic": "djangoforms", "completed": "true"},
        {"user": "user2", "topic": "drf", "completed": "true"},
        {"user": "user3", "topic": "drf", "completed": "true"},

    ]
    contaxt={}
    contaxt["timesheets"]=timesheets
    return render(request,"list_timesheet.html",contaxt)

# def add_accounts(request):
#     if request.method=="POST":
#         name=request.POST.get("u_name")
#         print(name)
#         fn = request.POST.get("fname")
#         print(fn)
#         e_mail = request.POST.get("email")
#         print(e_mail)
#         passs = request.POST.get("pass")
#         print(passs)
#         phn = request.POST.get("phone")
#         print(phn)
#         return render(request,"registration.html")
#     return render(request,"registration.html")

def view_login(request):
    if request.method=="GET":
        form=Loginform()
        contaxt={}
        contaxt["form"]=form

        return render(request,"login.html",contaxt)

    if request.method=="POST":
        form=Loginform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

            u_name=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            print(u_name,password)
            return redirect("log")


def list_batches(request):
    batches = [
        {"batch_code": "DJ-JUL-2k21", "batch_name": "djangojuly", "students": 25},
        {"batch_code": "DJ-AUG-2k21", "batch_name": "djangoaugest", "students": 30},
        {"batch_code": "MS-AUG-2k21", "batch_name": "meanstackaug", "students": 32},

    ]
    contaxt={}
    contaxt["batches"]=batches
    return render(request,"list_batches.html",contaxt)


def list_faculty(request):
    users = [
        {"user_name": "sabir", "domain": "BIG DATA"},
        {"user_name": "shifna", "domain": "DJANGO"},
        {"user_name": "rugma", "domain": "TESTING"}

    ]
    contaxt={}
    contaxt["users"]=users
    return render(request,"list_users.html",contaxt)


def Registration(request):
    if request.method=="GET":
        form=Registrationform()
        contaxt={}
        contaxt["form"]=form
        return render(request,"registration.html",contaxt)
    if request.method=="POST":
        form=Registrationform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            u_name = form.cleaned_data["username"]
            f_name = form.cleaned_data["firstname"]
            e_mail = form.cleaned_data["email"]
            pwd = form.cleaned_data["password"]
            ph_no = form.cleaned_data["phonenumber"]
            print(u_name,f_name,e_mail,pwd,ph_no)
            return redirect("registration")

