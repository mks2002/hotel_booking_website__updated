# mainapp we created for login details and login model table so here we serve all the pages related to user signup and login..

# import all basic rendering and redirecting modules...
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

# datetime module is used for deal with dates..
from datetime import datetime as dt

# this are all our models which we used in this section..

from mainapp.models import Login
from bookings.models import Bookinghotel

# we dont use Hotellist here..
# from hotellist.models import Hotellist


# this is for signup page...
def signup(request):
    n = ''
    cname = ''
    bool = False
    data = {'n': n,
            'bool': bool, 'cname': cname}
    if request.method == "POST":
        un = request.POST.get('name')
        pw = request.POST.get('password')
        cpw = request.POST.get('cpassword')
        if pw != cpw:
            n = "password and confirm password must be same"
            cname = "alert-danger"
            bool = 50
            data = {'n': n,
                    'bool': bool, 'cname': cname}
        else:
            if Login.objects.filter(username=un).exists():
                n = "username already exist select another"
                cname = "alert-warning"
                bool = 40
                data = {'n': n,
                        'bool': bool, 'cname': cname}
            else:
                maindata = Login(username=un, password=pw)
                maindata.save()
                n = 'You have registerd succesfully! now you can login '
                bool = 30
                cname = "alert-success"
                data = {'n': n,
                        'bool': bool, 'cname': cname}
                hl = "all"
                return render(request, 'signup.html', data)
    return render(request, 'signup.html', data)


def login(request):
    if request.method == "GET":
        n = "for booking you need to login first !"
        cname = "alert-warning"
        bool = False
        data = {'n': n,
                'cname': cname,
                'bool': bool}
        return render(request, 'login.html', data)

    if request.method == "POST":
        un = request.POST.get('name')
        pw = request.POST.get('password')
        if Login.objects.filter(username=un, password=pw).exists():
            hl = 'all'
            user = Login.objects.get(username=un, password=pw)
            request.session['user_{}_uname'.format(user.id)] = un
            request.session['user_{}_upass'.format(user.id)] = pw
            id = user.id
            url = "/hotellist/{}/{}".format(hl, id)
            return HttpResponseRedirect(url)
        else:
            n = "you are not registered create account to login "
            cname = "alert-danger"
            bool = 50
            data = {'n': n,
                    'cname': cname,
                    'bool': bool}
            return render(request, 'login.html', data)
    return render(request, 'login.html')


def logout_user(request, id):
    if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
        return HttpResponseRedirect('/login/')
    elif 'user_{}_uname'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session:
        user = Login.objects.get(
            username=request.session.get('user_{}_uname'.format(id)))
        del request.session['user_{}_uname'.format(user.id)]
        del request.session['user_{}_upass'.format(user.id)]
        request.session.flush()
        request.session.clear_expired()
    return HttpResponseRedirect('/signup/')

# this is for forgot password and this is before login ...


def update(request):
    n = 'enter your new password here'
    cname = 'alert-warning'
    bool = False
    data = {'n': n, 'bool': bool, 'cname': cname}
    if request.method == "POST":
        name = request.POST.get('name')
        new = request.POST.get('newpassword')
        cnew = request.POST.get('confirm_newpassword')
        if Login.objects.filter(username=name).exists():
            main = Login.objects.get(username=name)
            oldpassword = main.password

            if new == cnew:
                if new == oldpassword:
                    n = 'your new password is too similar to old password select another !'
                    cname = 'alert-warning'
                    bool = 70
                    data = {'n': n, 'bool': bool, 'cname': cname}
                else:
                    Login.objects.filter(username=name).update(
                        password=new)
                    # when we update the password we have to update it in the Bookinghotel table also othewise data is not properly displayed...
                    Bookinghotel.objects.filter(
                        username=name).update(userpassword=new)
                    n = 'your password is updated successfully now you can login !'
                    cname = 'alert-success'
                    bool = True
                    data = {'n': n, 'bool': bool, 'cname': cname}
            else:
                n = 'pasword and confirm password must be same'
                cname = 'alert-danger'
                bool = 60
                data = {'n': n, 'bool': bool, 'cname': cname}
        else:
            n = 'No such account is exist'
            cname = 'alert-danger'
            bool = 50
            data = {'n': n, 'bool': bool, 'cname': cname}
        return render(request, 'update_password.html', data)
    return render(request, 'update_password.html', data)


# we can also create one update password after the login .....
