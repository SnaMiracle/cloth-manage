"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myApp import category_views, views, product_views

urlpatterns = [
    # #product
    path("",views.home,name="/"),
    path("index/",views.index,name="index"),
    path("create/",views.create,name="create"),
    path("post/",views.post,name="post"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("edit/<int:id>",views.edit,name="edit"),
    path("update/<int:id>",views.update,name="update"),
    
    #user
    path("index_user/",views.index_user,name="index_user"),
    path("create_user/",views.create_user,name="create_user"),
    path("post_user/",views.post_user,name="post_user"),
    path("delete_user/<int:id>/",views.delete_user,name="delete_user"),
    path("edit_user/<int:id>/",views.edit_user,name="edit_user"),
    path("update_user/<int:id>/",views.update_user,name="update_user"),
    
    #category
    path("index_category/",views.index_category,name="index_category"),
    path("create_category/",views.create_category,name="create_category"),
    path("post_category/",views.post_category,name="post_category"),
    path("delete_category/<int:id>/",views.delete_category,name="delete_category"),
    path("edit_category/<int:id>/",views.edit_category,name="edit_category"),
    path("update_category/<int:id>/",views.update_category,name="update_category"),
    
    path("category/index/",category_views.index,name="category/index/"),
    path("category/create/",category_views.create,name="category/create/"),
    path("category/post/",category_views.post,name="category/post/"),
    path("category/delete_by_id/<int:id>",category_views.delete_by_id,name="category/delete_by_id/"),
    path("category/edit/<int:id>",category_views.edit,name="category/edit/"),
    path("category/update/<int:id>",category_views.update,name="category/update/"),
    #path("content/",category_views.content,name="content")
    
    #PRODUCT
    path("products/index/",product_views.index,name="products/index/"),
    path("products/create/",product_views.create,name="products/create/"),
    path("products/post/",product_views.post,name="products/post/"),
    path("products/delete_by_id/<int:id>",product_views.delete_by_id,name="products/delete_by_id/"),
    path("products/edit/<int:id>",product_views.edit,name="products/edit/"),
    path("products/update_by_id/<int:id>",product_views.update_by_id,name="products/update_by_id/"),


    
    
]
