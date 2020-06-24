from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 200)
    cat_image = models.ImageField(upload_to='shop/images/category', blank= True, default = '')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=800)
    price = models.IntegerField()
    discount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    product_image = models.ImageField(upload_to='shop/images/product', default = '')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name, self.id

class Order(models.Model):
    
    order_id = models.CharField(max_length=200)
    products_id = models.CharField(max_length=200)
    items_json = models.CharField(max_length=5000, default = '')
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True)
    total = models.IntegerField()
    discount = models.IntegerField()
    status = models.CharField(max_length=100, blank=True, null=True)
    tax = models.IntegerField()
    price = models.IntegerField()
    name = models.CharField(max_length=90, default = '')
    email = models.CharField(max_length=111, default = '')
    city = models.CharField(max_length=111, default = '')
    state = models.CharField(max_length=111, default = '')
    address = models.CharField(max_length=1000)
    pincode = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.order_id

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name      