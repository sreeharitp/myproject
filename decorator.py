from django.shortcuts import redirect


def user_login_required(func):
    def wrap(request,*args,**kwargs):
        if not (request.session.get('userid')):
            return redirect('/user/userhome')
        else:
            return func(request,*args,**kwargs)
    return wrap 