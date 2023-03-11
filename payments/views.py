from django.shortcuts import render
from django.http import HttpResponseRedirect
from bookings.models import Bookinghotel
from payments.models import Paymentdetail

from django.contrib import messages
from operator import not_
# Create your views here.


# session__id
# order_id


# this is for payment form page ..
def paymentpage(request):
    id = request.GET.get('session__id')
    if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
        return HttpResponseRedirect('/login/')
    elif 'user_{}_uname'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session:
        data = {}
        if request.method == "GET":
            id = request.GET.get('session__id')
            oid = request.GET.get('order_id')
            cost = request.GET.get('cost')
            maindata = Bookinghotel.objects.get(id=oid)
            un = maindata.username
            pw = maindata.userpassword
            url = "/dashboard/{}".format(id)
            data = {'id': id, 'url': url, 'un': un,
                    'pw': pw, 'cost': cost, 'oid': oid}
            return render(request, 'payment.html', data)
        try:
            if request.method == "POST":
                uname = request.POST.get('username')
                upass = request.POST.get('password')
                order_no = request.POST.get('order_no')
                total_cost = request.POST.get('total_cost')
                email = request.POST.get('email')
                card_no = request.POST.get('card_no')
                cvv_no = request.POST.get('cvv')
                exp_date = request.POST.get('exp_date')

                # this are get method variable....
                id = request.GET.get('session__id')
                oid = request.GET.get('order_id')
                cost = request.GET.get('cost')
                maindata = Bookinghotel.objects.get(id=oid)
                un = maindata.username
                pw = maindata.userpassword
                full_name = maindata.firstname + maindata.lastname
                url = "/dashboard/{}".format(id)
                if len(card_no) != 14:
                    messages.warning(request, 'invailed debit card number !')
                    data = {'id': id, 'url': url, 'un': un,
                            'pw': pw, 'cost': cost, 'oid': oid}
                    return render(request, 'payment.html', data)
                elif len(cvv_no) != 4 and len(cvv_no) != 3:
                    messages.warning(request, 'invailed cvv number !')
                    data = {'id': id, 'url': url, 'un': un,
                            'pw': pw, 'cost': cost, 'oid': oid}
                    return render(request, 'payment.html', data)
                elif len(exp_date) != 5:
                    messages.warning(request, 'invailed expiry date format it must be MM/YY !')
                    data = {'id': id, 'url': url, 'un': un,
                            'pw': pw, 'cost': cost, 'oid': oid}
                    return render(request, 'payment.html', data)
                elif (exp_date[0:2].isnumeric() and exp_date[3:5].isnumeric()) == False:
                    messages.warning(
                        request, 'invailed format of month or year they must be numeric !')
                    data = {'id': id, 'url': url, 'un': un,
                            'pw': pw, 'cost': cost, 'oid': oid}
                elif int(exp_date[0:2]) > 12:
                    messages.warning(
                        request, 'invailed value of month it must be less than or equal to 12 !')
                    data = {'id': id, 'url': url, 'un': un,
                            'pw': pw, 'cost': cost, 'oid': oid}
                    return render(request, 'payment.html', data)
                elif exp_date[2] != '/':
                    messages.warning(
                        request, 'please include a / between month and year !')
                    data = {'id': id, 'url': url, 'un': un,
                            'pw': pw, 'cost': cost, 'oid': oid}
                    return render(request, 'payment.html', data)

                else:
                    data1 = Paymentdetail(username=uname, password=upass, order_no=order_no,
                                          total_cost=total_cost, email=email, card_no=card_no, cvv=cvv_no, expiry_date=exp_date)
                    data1.save()
                    Bookinghotel.objects.filter(
                        id=order_no).update(payment_status='paid')
                    data = {'id': id, 'url': url}
                    messages.success(
                        request, f'your payment has been done successfully for the order of mr. {full_name} !')
                    response = HttpResponseRedirect(url)
                    return response
        except Exception as e:
            pass
    return render(request, 'payment.html', data)
