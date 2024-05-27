from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse

class Mobile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    model = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_time_created = models.DateTimeField(auto_now_add=True)
    date_time_edited = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='uploads/')


class Laptop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    model = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=50)
    date_time_created = models.DateTimeField(auto_now_add=True)
    date_time_edited = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='uploads/')

class MotherBoards(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    model = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=50)
    date_time_created = models.DateTimeField(auto_now_add=True)
    date_time_edited = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='uploads/')

class Desktop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    model = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=50)
    date_time_created = models.DateTimeField(auto_now_add=True)
    date_time_edited = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='uploads/')

class Accessories(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=50)
    date_time_created = models.DateTimeField(auto_now_add=True)
    date_time_edited = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='uploads/')

class ContactUs(models.Model):
    username = models.ForeignKey('auth.User' , on_delete=models.CASCADE)
    email = models.EmailField()
    description = models.TextField()

class OrderModel(models.Model):
    # class Meta:
    #     verbose_name = "سفارش"
    #     verbose_name_plural = "سفارش"     

    user = models.ForeignKey(User,on_delete= models.CASCADE,null=True,blank=True, default = 1)
    # accessories = models.ForeignKey(Accessories, on_delete= models.CASCADE, null=True)
    # desktop = models.ForeignKey(Desktop, on_delete= models.CASCADE, null=True,blank=True)
    # motherBoards = models.ForeignKey(MotherBoards, on_delete= models.CASCADE,null=True,blank=True)
    # mobile = models.ForeignKey(Mobile, on_delete= models.CASCADE, null=True,blank=True)
    laptop = models.ForeignKey(Laptop, on_delete= models.CASCADE, null=True,blank=True)

    # DayTimeOrder = models.DateTimeField(verbose_name = "زمان ارسال", default=datetime.now)

    

    def __str__(self):
        return f"userID :{self.user}, laptop id : {self.laptop}"