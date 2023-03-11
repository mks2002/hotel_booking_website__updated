
# import all basic rendering and redirecting modules...
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

# datetime module is used for deal with dates..
from datetime import date
from datetime import datetime as dt


# this are all our models which we used in this section..

from bookings.models import Bookinghotel

from mainapp.models import Login
from django.contrib import messages


def bookings(request, id):
    if f"user_{id}_uname" not in request.session or f"user_{id}_upass" not in request.session:
        return HttpResponseRedirect('/login/')
    elif 'user_{}_uname'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session:
        data1 = {}
        if request.method == "GET":
            un1 = request.session.get(f"user_{id}_uname")
            password1 = request.session.get(f"user_{id}_upass")
            hname1 = request.GET.get('hname')
            hcity1 = request.GET.get('hcity')
            hstate1 = request.GET.get('hstate')
            hcost1 = request.GET.get('hcost')
            # url = f"/dashboard/{id}"
            url = "/dashboard/{}".format(id)
            data1 = {'un1': un1, 'pw1': password1, 'hname1': hname1,
                     'hcity1': hcity1, 'hstate1': hstate1, 'hcost1': hcost1, 'url': url, 'id': id}
            return render(request, 'booking.html', data1)

        try:
            if request.method == "POST":
                name = request.POST.get('name')
                last = request.POST.get('last')
                email = request.POST.get('email')
                contact = request.POST.get('contact')
                person = request.POST.get('person')
                # these are hidden fields .....
                username = request.POST.get('username')
                password = request.POST.get('password')
                start = request.POST.get('startdate')
                end = request.POST.get('lastdate')
                hotelname = request.POST.get('hotelname')
                hotelcity = request.POST.get('hotelcity')
                hotelstate = request.POST.get('hotelstate')
                hotelcost = request.POST.get('hotelcost')

                # these are all the get method variable....
                un1 = request.session.get(f"user_{id}_uname")
                password1 = request.session.get(f"user_{id}_upass")
                hname1 = request.GET.get('hname')
                hcity1 = request.GET.get('hcity')
                hstate1 = request.GET.get('hstate')
                hcost1 = request.GET.get('hcost')

                if start < str(date.today()):
                    messages.warning(
                        request, 'Your starting date must be equal or more than today !')
                    url = f"/dashboard/{id}"

                    data1 = {'un1': un1, 'pw1': password1, 'hname1': hname1,
                             'hcity1': hcity1, 'hstate1': hstate1, 'hcost1': hcost1, 'url': url, 'id': id}
                    return render(request, 'booking.html', data1)
                elif start > end:
                    messages.warning(
                        request, 'your ending date must be more than start date !')

                    url = "/dashboard/{}".format(id)
                    data1 = {'un1': un1, 'pw1': password1, 'hname1': hname1,
                             'hcity1': hcity1, 'hstate1': hstate1, 'hcost1': hcost1, 'url': url, 'id': id}
                    return render(request, 'booking.html', data1)
                else:
                    data = Bookinghotel(firstname=name, lastname=last,
                                        email=email, contact_no=contact, no_people=person, username=username, userpassword=password, start=start, end=end, hotelname=hotelname, city=hotelcity, state=hotelstate, current_cost=hotelcost)
                    data.save()
                    url = "/dashboard/{}".format(id)
                    data1 = {'url': url, 'id': id}
                    # this is for redirecting into the dashboard page ...
                    response = HttpResponseRedirect(url)
                    messages.success(
                        request, 'Your booking has been done. You can see your order details below !')
                    return response
        except Exception as e:
            pass
    return render(request, 'booking.html', data1)


def dashboard(request, id):
    if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
        return HttpResponseRedirect('/login/')
    elif 'user_{}_uname'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session:
        data = {}
        username = request.session['user_{}_uname'.format(id)]
        password = request.session['user_{}_upass'.format(id)]
        if Login.objects.filter(username=username, password=password).exists():
            tabel = Bookinghotel.objects.filter(
                username=username, userpassword=password)
            hotelurl = '/hotellist/{}/{}'.format('all', id)
            reviewurl = '/review/{}'.format(id)
            # this url is for dashboard page itself ....
            url = "/dashboard/{}".format(id)
            data = {'un': username, 'pw': password, 'id': id,
                    'maindata': tabel, 'hotelurl': hotelurl, 'reviewurl': reviewurl, 'url': url}
            return render(request, 'dashboard.html', data)
        return render(request, 'dashboard.html', data)


# this is for order details page..
def details(request):
    id = request.GET.get('session__id')
    if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
        return HttpResponseRedirect('/login/')
    elif 'user_{}_uname'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session:
        data = {}
        if request.method == "GET":
            id = request.GET.get('session__id')
            detail_id = request.GET.get('id1')
            un = request.session['user_{}_uname'.format(id)]
            password = request.session['user_{}_upass'.format(id)]

            url = "/dashboard/{}".format(id)
            maindata = Bookinghotel.objects.get(id=detail_id)
            bool = (maindata.payment_status.lower() == 'unpaid')
            start = str(maindata.start)
            end = str(maindata.end)
            res = (dt.strptime(end, "%Y-%m-%d") -
                   dt.strptime(start, "%Y-%m-%d")).days
            total_cost = res*maindata.current_cost
            data = {'un': un, 'pw': password,
                    'maindata': maindata, 'url': url, 'cost': total_cost, 'id': id, 'bool': bool, 'order_id': detail_id, 'bool': bool}
            return render(request, 'order_details.html', data)
        return render(request, 'order_details.html', data)

# in each page context we have to pass the id value because it is the session key variable so we use this so that we can check if someone is logged in or logged out ...

# this page is for deleting the order...

# for deleting the order ...
def delete(request):
    id = request.GET.get('session__id')
    if 'user_{}_uname'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session:
        id1 = request.GET.get('id1')
        id = request.GET.get('session__id')
        Bookinghotel.objects.filter(id=id1).delete()
        url = "/dashboard/{}".format(id)
        return HttpResponseRedirect(url)
