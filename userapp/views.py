from django.shortcuts import render

# Create your views here.
def masterFn(request):
    return render(request,'master1.html')
def userhomeFn(request):
    return render(request,'userhome.html')    
def userhome2Fn(request):
    return render(request,'userhome2.html')
def userhome3Fn(request):
    return render(request,'userhome3.html')
def aboutFn(request):
    return render(request,'aboutus.html')
def contactFn(request):
    return render(request,'contactus.html')        
def regFn(request):
    return render(request,'evereg.html')            