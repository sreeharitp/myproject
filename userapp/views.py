from django.shortcuts import redirect, render

from userapp.models import Userdetails
from decorator import user_login_required 

# Create your views here.


def masterFn(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        mobile = request.POST['phone']
        place = request.POST['place']
        password = request.POST['password']
        userDetails = Userdetails(firstName=firstname, lastName=lastname,
                                  email=email, mobile=mobile, place=place, password=password)
        userDetails.save()
        return render(request, 'userhome.html', {'status': 1})
    else:
        return render(request, 'userhome.html', {'status': 0})


def userloginFn(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            data = Userdetails.objects.get(email=email, password=password)
            request.session['userid'] = data.id
            return render(request, 'userhome.html', {'error': 1})
        except Userdetails.DoesNotExist:
            return render(request, 'userhome.html')
    else:
        return render(request, 'userhome.html')


def userlogoutFn(request):
    del request.session['userid']
    return redirect('/user/userhome')


def userhomeFn(request):
    return render(request, 'userhome.html')


def userhome2Fn(request):
    return render(request, 'userhome2.html')


def userhome3Fn(request):
    return render(request, 'userhome3.html')


def aboutFn(request):
    return render(request, 'aboutus.html')


def contactFn(request):
    return render(request, 'contactus.html')

@user_login_required
def regFn(request):
    return render(request, 'evereg.html')


def payFn(request):
    return render(request, 'userpayment.html')


def profileFn(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['useremail']
        mobile = request.POST['usermobile']
        place = request.POST['userplace']
        update = Userdetails.objects.filter(id=request.session['userid']).update(
            firstName=firstname, lastName=lastname, email=email, mobile=mobile, place=place)
        return redirect('userprofile')
    else:
        uid = request.session['userid']
        userDetail = Userdetails.objects.get(id=uid)
        return render(request, 'userprofile.html', {'details': userDetail})
