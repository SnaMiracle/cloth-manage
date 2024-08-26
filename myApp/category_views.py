from django.shortcuts import redirect, render
from django.contrib import messages

from myApp.models import Category

def index(request):
    categorys=Category.objects.all()
    data={"categorys":categorys}
    return render(request,"pages/categorys/index.html",data)

def create(request):
    return render(request,"pages/categorys/create.html")

def post(request):
    category=Category()
    category.category_name=request.POST["category_name"]
    category.save()
    messages.success(request,"Category created")
    return redirect("/category/create/")

def delete_by_id(request,id):
    category=Category.objects.filter(id=id)
    category.delete()
    return redirect("/category/index/")

def edit(request,id):
    category=Category.objects.filter(id=id).first()
    data={"category":category}
    return render(request,"pages/categorys/edit.html",data)

def update(request,id):
    category=Category.objects.filter(id=id).first()
    category.category_name=request.POST["category_name"]
    category.save()
    messages.success(request,"Category updated")
    return redirect("/category/edit/"+str(id))
    
# def content(request):
#     # categorys=Category.objects.all()
#     # data={"categorys":categorys}
#     # return render(request,"pages/categorys/content.html",data)
#     return render(request,"pages/categorys/content.html")