from employer import forms
from employer.models import Employerprofile
from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy


# class Profileview(CreateView):
#     model = Employerprofile
#     form_class = forms.Employerprofile
#     template_name = "create_profile.html"
#     # context_object_name = "employer"
