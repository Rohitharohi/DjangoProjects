from django.shortcuts import render,redirect
from Book import forms
from Book.models import Book
# Create your views here.

def Add_book(request):
    if request.method=="GET":
        form=forms.Bookform(initial={"price":0,"copies":0})
        context={}
        context["form"]=form
        return render(request,"book_add.html",context)

    if request.method=="POST":
        form=forms.Bookform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # print(form.cleaned_data)
            # book_name=form.cleaned_data["book_name"]
            # author=form.cleaned_data["author"]
            # price=form.cleaned_data["price"]
            # copies=form.cleaned_data["availability"]
            # books=Book.objects.create(book_name=book_name,author=author,price=price,copies=copies)
            # books.save()
            print("book saved")
            return redirect("list")

        else:
            return render(request,"book_add.html",{"form":form})

def list_book(request):
    books=Book.objects.all()
    context={}
    context["books"]=books
    return render(request,"list_book.html",context)


def remove_book(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect("list")

def change_book(request,id):
    book=Book.objects.get(id=id)
    if request.method=="GET":
        # form=forms.Bookform(initial={"book_name":book.book_name,
        #     "author":book.author,
        #     "price":book.price,
        #     "availability":book.copies})
        form=forms.Bookform(instance=book)
        context={}
        context["form"]=form
        return render(request,"book_edit.html",context)
    if request.method=="POST":
        form=forms.Bookform(request.POST,instance=book)
        if form.is_valid():
            form.save()
            # book_name=form.cleaned_data["book_name"]
            # author=form.cleaned_data["author"]
            # price=form.cleaned_data["price"]
            # availability=form.cleaned_data["availability"]
            # book.book_name=book_name
            # book.author=author
            # book.price=price
            # book.copies=availability
            # book.save()
            return redirect("list")
def book_details(request,id):
    book=Book.objects.get(id=id)
    context={}
    context["book"]=book
    return render(request,"book_details.html",context)

