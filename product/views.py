from django.shortcuts import render
from .models import Product

def product(request):
          obj=Product.objects.all()
          context ={
                   "obj":obj
                   
          }
          
          return render(request,'product/product.html',context)