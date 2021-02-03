from pages.forms import LoginForm
from django.shortcuts import render
from .models import Login
from .forms import LoginForm

def pages(request):
          data=LoginForm(request.POST)
          data.save()
          context={
                    "lf":LoginForm,
          }
  

          
          return render(request,'pages/page.html',context)