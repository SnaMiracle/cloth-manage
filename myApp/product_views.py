from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.decorators.http import require_http_methods


from myApp.models import Category, Product


@require_http_methods(["GET"])
def index(request):
    products=Product.objects.all()
    data={"products":products}
    return render(request,"pages/products/index.html",data)

@require_http_methods(["GET"])
def create(request):
    categorys=Category.objects.all()
    data={"categorys":categorys}
    return render(request,"pages/products/create.html",data)

@require_http_methods(["POST"])
def post(request):
    product=Product()
    product.product_name=request.POST["product_name"]
    product.barcode=request.POST["barcode"]
    product.sell_price=request.POST["sell_price"]
    product.qty_instock=request.POST["qty"]
    product.create_by=1
    product.category_id=request.POST["dllcategory_id"]
    if len(request.FILES)>0:
        product.photo=request.FILES["file"]
        product.save()
    else:
        product.photo="";
        product.save()
    messages.success(request,"Product created")
    return redirect("products/create/")

def delete_by_id(request,id):
    product=Product.objects.filter(id=id).first()
    product.photo.delete()
    product.delete()
    return redirect("products/index/")

def edit(request,id):
    product=Product.objects.get(pk=id)
    categorys=Category.objects.all()
    data={"product":product,"categorys":categorys}
    return render(request,"pages/products/edit.html",data)

def update_by_id(request,id):
    product=Product.objects.get(pk=id)
    product.product_name=request.POST["product_name"]
    product.barcode=request.POST["barcode"]
    product.sell_price=request.POST["sell_price"]
    product.qty_instock=request.POST["qty"]
    product.update_by=1
    product.category_id=request.POST["dllcategory_id"]
    if product.photo:
        if len(request.FILES)>0:
            product.photo.delete()
            product.photo=request.FILES["file"]
            product.save()
            messages.success(request,"Product updated")

        else:
            product.save()
            messages.success(request,"Product updated")
    else:
        if len(request.FILES)>0:
            product.photo=request.FILES["file"]
            product.save()
            messages.success(request,"Product updated")

        else:
            product.save()
            messages.success(request,"Product updated")
    return redirect("products/create/")