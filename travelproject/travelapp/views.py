from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def demo(request):

    return render(request,"index.html")

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{'result':res})
