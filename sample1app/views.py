from django.shortcuts import render

# Create your views here.
def loadfirst(request):
    return render(request,'first.html')
def loadsecond(request):
    return render(request,'second.html')