from django.http import HttpResponse
from django.shortcuts import redirect, render

from myApp.models import Product, User, Category

# Create your views here.
# product
product_lists=[
        Product(1,"ABC",1111,1,1.5),
        Product(2,"Tiger",2222,1,2),
        Product(3,"Fanta",3333,0.5,1)
            ]
user_list=[
    User(1,"Thida","Female","1111"),
    User(2,"Seyha","Male","2222"),
    User(3,"Dara","Male","3333")
]
category_list=[
    Category(1,"Beverage"),
    Category(2,"Snack"),
    Category(3,"Beer")
]

def home(request):
    return  render(request,"home.html")
def index(request):
    data={"products":product_lists,"id":1}
    return render(request,"product/index.html",data)
def create(request):
    return render(request,"product/create.html")
def post(request):
    product=Product()
    product.id=4;
    product.name=request.POST["name"]
    product.barcode=request.POST["barcode"]
    product.unit_price = request.POST["unit_price"]
    product.sell_price = request.POST["sell_price"]
    product_lists.append(product)
    return redirect("/create")

def delete(request,id):
    for col in product_lists:
        if col.id==id:
            product_lists.remove(col)
    return redirect("/index")
def edit(request,id):
    data=None
    for col in product_lists:
        if col.id==id:
            data={"product":col}
    return render(request,"product/edit.html",data)
def update(request,id):
    for col in product_lists:
        if col.id==id:
            col.name=request.POST["name"]
            col.barcode=request.POST["barcode"]
            col.unit_price=request.POST["unit_price"]
            col.sell_price=request.POST["sell_price"]
    return redirect("/edit/"+str(id))

#user
def index_user(request):
    data_user={"users":user_list,"id":1}
    return render(request, "user/index_user.html",data_user)
def create_user(request):
    return render(request,"user/create_user.html")
def post_user(request):
    user=User()
    user.id=4;
    user.name=request.POST["name"]
    user.gender = request.POST["gender"]
    user.password = request.POST["password"]
    user_list.append(user)
    return redirect("/create_user/")

def delete_user(request,id):
    for col in user_list:
        if col.id==id:
            user_list.remove(col)
    return redirect("/index_user/")
def edit_user(request,id):
    data=None
    for col in user_list:
        if col.id==id:
            data={"user":col}
    return render(request,"user/edit_user.html",data)
def update_user(request,id):
    for col in user_list:
        if col.id==id:
            col.name=request.POST["name"]
            col.gender = request.POST["gender"]
            col.password = request.POST["password"]
    return redirect("/edit_user/"+str(id))

#category
def index_category(request):
    data={"categorys":category_list,"id":1}
    return render(request, "category/index_category.html",data)
def create_category(request):
    return render(request,"category/create_category.html")
def post_category(request):
    category=Category()
    category.id=4;
    category.Cat_name=request.POST["Cat_name"]
    category_list.append(category)
    return redirect("/create_category/")

def delete_category(request,id):
    for col in category_list:
        if col.id==id:
            category_list.remove(col)
    return redirect("/index_category/")
def edit_category(request,id):
    data=None
    for col in category_list:
        if col.id==id:
            data={"category":col}
    return render(request,"category/edit_category.html",data)
def update_category(request,id):
    for col in category_list:
        if col.id==id:
            col.Cat_name=request.POST["Cat_name"]
    return redirect("/edit_category/"+str(id))

