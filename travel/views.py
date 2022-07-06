from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,Team


def demo(request):
    obj=Place.objects.all()
    obj2=Team.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj2})
#
# def about(request):
#     return render(request,"about.html")
#
# def contact(request):
#     return HttpResponse("this is my contact number")
# def operation(request):
#     return render(request,"operation.html")
# def result(request):
#     x=int(request.GET["num1"])
#     y=int(request.GET['num2'])
#     add=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     return render(request,"result.html",{'a':add,'s':sub,'m':mul,'d':div})