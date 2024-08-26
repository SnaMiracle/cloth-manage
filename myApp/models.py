import datetime
from django.db import models

# Create your models here.
#product
class Product(models.Model):
    product_name=models.CharField(max_length=20,unique=True,null=False)
    barcode=models.BigIntegerField(unique=True,null=False)
    sell_price=models.FloatField()
    qty_instock=models.IntegerField()
    photo=models.ImageField(upload_to="media/",null=True,blank=True)
    category=models.ForeignKey("Category",on_delete=models.CASCADE)
    create_by=models.BigIntegerField()
    update_by=models.BigIntegerField(null=True,blank=True)
    create_at=models.DateTimeField(auto_now=datetime.datetime.now())
    update_at=models.DateTimeField(null=True,blank=True)
    

#user
class User:
    id=None
    username=None
    gender=None
    password=None
    def __init__(self, id="", name="", gender="", password=""):
        self.id = id
        self.name = name
        self.gender = gender
        self.password = password
        
#category
class Category:
    id=None
    Cat_name=None
    def __init__(self, id="", Cat_name=""):
        self.id = id
        self.Cat_name = Cat_name
        
class Category(models.Model):
    category_name=models.CharField(max_length=10)