from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Book(models.Model):
    book_name=models.CharField(unique=True,max_length=100)
    author=models.CharField(max_length=100)
    price=models.PositiveIntegerField(max_length=100)
    copies=models.PositiveIntegerField(max_length=100)
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.book_name

class Cart(models.Model):
    item=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(("incart","incart"),
             ("orderplaced","orderplaced"),
             ("remove","remove"))
    status=models.CharField(max_length=150,choices=options,default="incart")



# 1

# books=Book(book_name="oru desathine kadha",author="sk",price=700,copies=7)
# books.save()

# 2..print all books

# books=Book.objects.all()
# books

# 3..print price and book_name

# for book in books:
#  (tab space) print(book.book_name,book.price)
# enter
# enter

# 4..less than 160

# books = Book.objects.filter(price__lt=160)
# books

# 5...greater than 160

# books = Book.objects.filter(price__gt=2000)
# books

# 6...range

 # books=Book.objects.filter(price__lt=200,price__gt=100)
 # books

 # 7..case insensitive

#books=Book.objects.filter(book_name__iexact="Randamoozham")
# books

# 8...

 #books=Book.objects.filter(book_name__contains="oru")
 # books

# 9..fetching perticular object(and delete)

#book=Book.objects.get(mobile_name="randamoozham")
# book.delete()

# 10..print id and book_name

# books=Book.objects.all().values('id','book_name')
# books

# 11..update ORM query

#book=Book.objects.get(id=5)
# book.price
# book.price=170
# book.copies=12