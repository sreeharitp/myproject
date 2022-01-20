from django.shortcuts import render

# Create your views here.
def adminFn(request):
    return render(request,'master2.html')
def eventFn(request):
    return render(request,'adminevent.html')
def dashFn(request):
    return render(request,'admindash.html')
def custFn(request):
    return render(request,'customer.html')
def payFn(request):
    return render(request,'adminpay.html') 
def rateFn(request):
    return render(request,'adminrating.html')  
def addFn(request):
    return render(request,'addteam.html')           
def viewFn(request):
    return render(request,'custview.html')               