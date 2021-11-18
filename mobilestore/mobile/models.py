from django.db import models
from django.contrib.auth.models import User


class Mobile(models.Model):
    mobile_name=models.CharField(unique=True,max_length=50)
    color=models.CharField(max_length=70)
    ram=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    availability=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.mobile_name
mobile=Mobile(mobile_name="realme",color="blue",ram=4,price=10000,availability=1)

class Cart(models.Model):
    item=models.ForeignKey(Mobile,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(("incart","incart"),
             ("cancelled","cancelled"),
             ("orderplaced","orderplaced"))
    status=models.CharField(max_length=150,choices=options,default="incart")

# class Cart(models.Model):
#     item=models.ForeignKey(Mobile,on_delete=models.CASCADE)
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     options=(("incart","incart"),
#              ("cancelled","cancelled"),
#              ("orderplaced","orderplaced"))
#     status=models.CharField(max_length=150,choices=options,default="incart")


class Orders(models.Model):
    item=models.ForeignKey(mobile,on_delete=models.CASCADE)
    user=models.CharField(max_length=40)
    address=models.CharField(max_length=120)
    date_order=models.DateField(auto_now_add=True)
    # orderplaced,dispatch,intransit,delivered,order_cancelled
    options=(
        ("orderplaced","oredrplaced"),
        ("dispatch","dispatch"),
        ("intransit","intransit"),
        ("delivered","delivered"),
        ("order_cancelled","order_cancelled")
    )
    status=models.CharField(max_length=120,choices=options,default="orderplaced")
    expected_delivery_date=models.DateField(null=True,blank=True)

# 1

# mobile=Mobile(mobile_name="huawei",color="blue",ram=4,price=7000,availability=7)
# mobile.save()

# 2..print all mobiles

# mobiles=Mobile.objects.all()
# mobiles

# 3..print price and mobile_name

# for mobile in mobiles:
#  (tab space) print(mobile.mobile_name,mobile.price)
# enter
# enter

# 4..less than 16000

# mobiles = Mobile.objects.filter(price__lt=16000)
# mobiles

# 5...greater than 16000

# mobiles = Mobile.objects.filter(price__gt=2000)
# mobiles

# 6...range

 # mobies=Mobile.objects.filter(price__lt=20000,price__gt=10000)
 # mobiles

 # 7..case insensitive

# mobiles=Mobile.objects.filter(mobile_name__iexact="Iphone")
# mobiles

# 8...

 # mobiles=Mobile.objects.filter(mobile_name__contains="iph")
 # mobiles

# 9..fetching perticular object(and delete)

# mobile=Mobile.objects.get(mobile_name="huawei")
# mobile.delete()

# 10..print id and mobile_name

# mobiles=Mobile.objects.all().values('id','mobile_name')
# mobiles

# 11..update ORM query

#mobile=Mobile.objects.get(id=5)
# mobile.price
# mobile.price=17000
# mobile.availability=12