from django.shortcuts import render

# Create your views here.
def master3Fn(request):
    return render(request,'master3.html')
def bookFn(request):
    return render(request,'booking.html')    
def finishFn(request):
    return render(request,'finished.html')  
def editFn(request):
    return render(request,'profedit.html')     
def createFn(request):
    return render(request,'profcrt.html')    
def evedashFn(request):
    return render(request,'eventdash.html')     
def evepayFn(request):
    return render(request,'eventpay.html')           
                           