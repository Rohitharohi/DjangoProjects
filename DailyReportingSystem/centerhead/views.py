from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView
from centerhead.models import Course,Batch
from centerhead import forms
from django.urls import reverse_lazy
from reportingsystem.models import MyUser
from datetime import date
# Create your views here.


class Adminhome(TemplateView):
    template_name = "centerhead/adminhome.html"


class Courseadd(CreateView):
    model = Course
    form_class = forms.CourseForm
    template_name = "centerhead/addcourse.html"
    success_url = reverse_lazy("coursedd")

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["courses"]=self.model.objects.all()
        return context


class Batchadd(CreateView):
    model = Batch
    form_class = forms.BatchForm
    template_name = "centerhead/batches.html"
    success_url = reverse_lazy("batchadd")

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["batches"]=self.model.objects.all()
        return context


class Updatebatch(UpdateView):
    model = Batch
    form_class = forms.UpdateBatch
    template_name = "centerhead/updatebatch.html"
    success_url = reverse_lazy ("batchadd")
    pk_url_kwarg = "id"

class Listbatch(ListView):
    model = Batch
    template_name = "centerhead/listbatch.html"
    context_object_name = "batches"


class Updatecourse(UpdateView):
    model = Course
    form_class = forms.Updatevourse
    template_name = "centerhead/updatecourse.html"
    success_url = reverse_lazy("coursedd")
    pk_url_kwarg = "id"



class Employees(CreateView):
    template_name = "centerhead/employees.html"
    model = MyUser
    form_class = forms.EmployeeForm
    success_url = reverse_lazy("employees")

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["employees"]=self.model.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            employee=form.save(commit=False)
            emp=MyUser.objects.create_user(email=employee.email,phonenumber=employee.phonenumber,role=employee.role,password=employee.password)
            emp.save()
            return redirect("employees")







