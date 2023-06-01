from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hardik(request):
    return render(request,'hardik.html')