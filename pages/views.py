from django.shortcuts import render
from .models import Female,Male

def pages(request):
          obj=Pages.objects.all()
          context ={
                   "obj":obj
                   
          }
          
          return render(request,'pages/page.html',context)