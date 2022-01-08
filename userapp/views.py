from django.shortcuts import render

# Create your views here.
def Masterfn(request):
    return render(request,'master.html')
def HomeFn(request):
    return render(request,'home.html')    
def Home2Fn(request):
    return render(request,'home2.html')
def Home3Fn(request):
    return render(request,'home3.html')