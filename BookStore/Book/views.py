from django.shortcuts import render,redirect
from Book import forms
from Book.models import Book,Orders
from django.views.generic import TemplateView,CreateView,ListView,DetailView,DeleteView,UpdateView
from django.urls import reverse_lazy
from .decorators import signin_required,admin_permission_required
from django.utils.decorators import method_decorator

# Create your views here.
def Adminhome(request):
    return render(request,"adminpage.html")

@method_decorator(admin_permission_required,name="dispatch")
class Bookcreateview(CreateView):
    model=Book
    form_class = forms.Bookform
    template_name = "book_add.html"
    success_url = reverse_lazy("list")



# class Addbook(TemplateView):
#     def get(self, request, *args, **kwargs):
#         form=forms.Bookform(initial={"price":0,"copies":0})
#         context={}
#         context["form"]=form
#         return render(request,"book_add.html",context)
#     def post(self,request):
#         form=forms.Bookform(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             print("book saved")
#             return redirect("list")
#
#         else:
#             return render(request, "book_add.html", {"form": form})



# def Add_book(request):
#     if request.method=="GET":
#         form=forms.Bookform(initial={"price":0,"copies":0})
#         context={}
#         context["form"]=form
#         return render(request,"book_add.html",context)

    # if request.method=="POST":
    #     form=forms.Bookform(request.POST,request.FILES)
    #     if form.is_valid():
    #         form.save()
            # print(form.cleaned_data)
            # book_name=form.cleaned_data["book_name"]
            # author=form.cleaned_data["author"]
            # price=form.cleaned_data["price"]
            # copies=form.cleaned_data["availability"]
            # books=Book.objects.create(book_name=book_name,author=author,price=price,copies=copies)
            # books.save()
        #     print("book saved")
        #     return redirect("list")
        #
        # else:
        #     return render(request,"book_add.html",{"form":form})


@method_decorator(admin_permission_required,name="dispatch")
class Listbook(ListView):
    model=Book
    template_name = "list_book.html"
    context_object_name = "books"




# class Listbook(TemplateView):
#     def get(self, request, *args, **kwargs):
#         books = Book.objects.all()
#         context = {}
#         context["books"] = books
#         return render(request, "list_book.html", context)

# def list_book(request):
#     books=Book.objects.all()
#     context={}
#     context["books"]=books
#     return render(request,"list_book.html",context)

@method_decorator(admin_permission_required,name="dispatch")
class Removebook(DeleteView):
    model=Book
    template_name = "remove.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("list")


@method_decorator(admin_permission_required,name="dispatch")
class Bookupdate(UpdateView):
    model = Book
    form_class =forms.Bookform
    template_name = "book_edit.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("list")


# def remove_book(request,id):
#     book=Book.objects.get(id=id)
#     book.delete()
#     return redirect("list")

# class Changebook(TemplateView):
#     model = Book
#     template_name = "book_edit.html"
#     context = {}
#     def get(self, request, *args, **kwargs):
#         id = kwargs["id"]
#         book = self.model.objects.get(id=id)
#         form = forms.Bookform(instance=book)
#
#         self.context["form"]=form
#         return render(request,"book_edit.html",self.context)
#     def post(self,request):
#         book = self.model.objects.get(id=id)
#
#         form = forms.Bookform(request.POST,instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect("list")






# def change_book(request,id):
#     book=Book.objects.get(id=id)
#     if request.method=="GET":

        # form=forms.Bookform(initial={"book_name":book.book_name,
        #     "author":book.author,
        #     "price":book.price,
        #     "availability":book.copies})

    #     form=forms.Bookform(instance=book)
    #     context={}
    #     context["form"]=form
    #     return render(request,"book_edit.html",context)
    # if request.method=="POST":
    #     form=forms.Bookform(request.POST,instance=book)
    #     if form.is_valid():
    #         form.save()

            # book_name=form.cleaned_data["book_name"]
            # author=form.cleaned_data["author"]
            # price=form.cleaned_data["price"]
            # availability=form.cleaned_data["availability"]
            # book.book_name=book_name
            # book.author=author
            # book.price=price
            # book.copies=availability
            # book.save()

            # return redirect("list")

# class Bookdetails(TemplateView):
#     def get(self, request, *args, **kwargs):
#         book = Book.objects.get(id=id)
#         context = {}
#         context["book"] = book
#         return render(request, "book_details.html", context)

@method_decorator(admin_permission_required,name="dispatch")
class Bookdetail(DetailView):
    model=Book
    template_name = "book_details.html"
    context_object_name = "book"
    pk_url_kwarg = "id"
# def book_details(request,id):
#     book=Book.objects.get(id=id)
#     context={}
#     context["book"]=book
#     return render(request,"book_details.html",context)

@method_decorator(admin_permission_required,name="dispatch")
class Vieworders(ListView):
    model = Orders
    template_name = "customer_order.html"
    context_object_name = "orders"

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        neworders=self.model.objects.filter(status="orderplaced")
        context["neworders"]=neworders
        d_orders = self.model.objects.filter(status="delivered")
        context["d_orders"] = d_orders

        context["newordercount"]=neworders.count()
        context["d_ordercount"]=d_orders.count()

        return context

        # context["d_ordercount"] = d_orders.count()

@method_decorator(admin_permission_required,name="dispatch")
class Viewneworderedbook(DetailView):
    model=Orders
    template_name = "newordered_book.html"
    context_object_name = "book"
    pk_url_kwarg = "id"



@method_decorator(admin_permission_required,name="dispatch")
class OrderUpdateview(UpdateView):
    model = Orders
    form_class = forms.Updateform
    template_name = "orderupdate.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("list")



