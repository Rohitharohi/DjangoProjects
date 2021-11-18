from django.shortcuts import render,redirect
from telecaller import forms
from telecaller.models import Enquiries

from django.views.generic import TemplateView,CreateView,ListView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from datetime import date

# Create your views here.
def home(request):
    return render(request,"base.html")

class Signinview(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.Loginform()
        context = {"form": form}
        return render(request, "login.html", context)

    def post(self, request):
        form = forms.Loginform(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if (user):
                login(request, user)
                if request.user.role=="telecaller":
                    return redirect("home")
                else:
                    return redirect("employees")
            return render(request,"home.html")
        else:
            context = {"form": form}
            return render(request, "login.html", context)

def Signout(request):
    logout(request)
    return redirect("login")


class EnquiryCreateView(CreateView):
    model = Enquiries
    form_class = forms.Enquiryform
    template_name = "addenquiry.html"
    success_url = reverse_lazy("enquiries")

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            enquiry=form.save(commit=False)
            enquiry.created_by=request.user
            enquiry.save()
            return redirect("enquiries")

class Listenquiries(ListView):
    template_name = "list_enquiries.html"
    model = Enquiries
    context_object_name = "enquiries"

#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         context["enquiries"]=self.model.objects.all()
#         return context

    def get_queryset(self):
        user=self.request.user
        return self.model.objects.filter(created_by=user)

class Followups(ListView):
    model = Enquiries
    template_name = "followups.html"
    context_object_name = "followups"

    def get_queryset(self):
        user=self.request.user
        return self.model.objects.filter(created_by=user,followupdate=date.today())


class ViewReports(ListView):
    template_name = "reports.html"
    model = Enquiries
    context_object_name = "reports"


    def get_context_data(self, *args, **kwargs):
        context=super().get_context_data(**kwargs)
        user = self.request.user
        count = self.model.objects.filter(enquirydate=date.today(), created_by=user).count()
        context["reports"]=count

        # admissioncount=self.model.objects.filter(equirydate=date.today(),created_by=user,status="admitted").count
        # context["admotioncount"]=admissioncount
        form=forms.Dateform()
        context["form"]=form
        return context
    def post(self,request,*args,**kwargs):
        form=forms.Dateform(self.request.POST)
        if form.is_valid():
            from_date=form.cleaned_data["from_date"]
            to_date=form.cleaned_data["to_date"]
            admissioncount=self.model.objects.filter(created_by=request.user,status="admitted",enquirydate__gte=from_date,enquirydate__lte=to_date).count()
            print(admissioncount)
            return redirect("report")




