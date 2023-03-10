# here in this file i have write all the view functions at one place this is for testing purpose.....


# import all basic rendering and redirecting modules...
# from userreview.models import Review
# import requests
# from django.http import HttpResponse, HttpResponseRedirect
# from hotellist.models import Hotellist
# from django.http import HttpResponse
# from django.shortcuts import render
# from django.http import HttpResponseRedirect

# # datetime module is used for deal with dates..
# from datetime import datetime as dt

# # this are all our models which we used in this section..

# from bookings.models import Bookinghotel

# from mainapp.models import Login


# def bookings(request, id):
#     if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
#         return HttpResponseRedirect('/login/')
#     elif 'user_{}_uname'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session:
#         data = {}
#         data1 = {}
#         bool = False
#         if request.method == "GET":
#             un1 = request.session.get('user_{}_uname'.format(id))
#             password1 = request.session.get('user_{}_upass'.format(id))
#             hname1 = request.GET.get('hname')
#             hcity1 = request.GET.get('hcity')
#             hstate1 = request.GET.get('hstate')
#             hcost1 = request.GET.get('hcost')
#             url = "/dashboard/{}".format(id)
#             data = {'un1': un1, 'pw1': password1, 'hname1': hname1,
#                     'hcity1': hcity1, 'hstate1': hstate1, 'hcost1': hcost1, 'url': url, 'id': id}
#             return render(request, 'booking.html', data)
#         try:
#             if request.method == "POST":
#                 name = request.POST.get('name')
#                 last = request.POST.get('last')
#                 email = request.POST.get('email')
#                 contact = request.POST.get('contact')
#                 person = request.POST.get('person')
#                 # this are hidden fields .....
#                 username = request.POST.get('username')
#                 password = request.POST.get('password')
#                 start = request.POST.get('startdate')
#                 end = request.POST.get('lastdate')
#                 hotelname = request.POST.get('hotelname')
#                 hotelcity = request.POST.get('hotelcity')
#                 hotelstate = request.POST.get('hotelstate')
#                 hotelcost = request.POST.get('hotelcost')

#                 #  this are all the get method variable....
#                 un1 = request.session.get('user_{}_uname'.format(id))
#                 password1 = request.session.get('user_{}_upass'.format(id))
#                 hname1 = request.GET.get('hname')
#                 hcity1 = request.GET.get('hcity')
#                 hstate1 = request.GET.get('hstate')
#                 hcost1 = request.GET.get('hcost')

#                 if end < start:
#                     class_name = 'alert-warning'
#                     bool = 50
#                     n = 'your starting date must be less than ending date'
#                     url = "/dashboard/{}".format(id)
#                     data1 = {'cname': class_name,
#                              'bool': bool,
#                              'n': n, 'un': username, 'pw': password, 'url': url, 'id': id, 'un1': un1, 'pw1': password1, 'hname1': hname1,
#                              'hcity1': hcity1, 'hstate1': hstate1, 'hcost1': hcost1}
#                     return render(request, 'booking.html', data1)
#                 else:
#                     data = Bookinghotel(firstname=name, lastname=last,
#                                         email=email, contact_no=contact, no_people=person, username=username, userpassword=password, start=start, end=end, hotelname=hotelname, city=hotelcity, state=hotelstate, current_cost=hotelcost)
#                     data.save()
#                     class_name = 'alert-success'
#                     bool = True
#                     n = 'your bookings has been done now'
#                     url = url = "/dashboard/{}".format(id)
#                     data1 = {'cname': class_name,
#                              'bool': bool,
#                              'n': n, 'un': username, 'pw': password, 'url': url, 'id': id, 'un1': un1, 'pw1': password1, 'hname1': hname1,
#                              'hcity1': hcity1, 'hstate1': hstate1, 'hcost1': hcost1}
#                     return render(request, 'booking.html', data1)
#         except Exception as e:
#             pass
#         return render(request, 'booking.html', data1)


# def dashboard(request, id):
#     if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
#         return HttpResponseRedirect('/login/')
#     elif 'user_{}_uname'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session:
#         data = {}
#         username = request.session['user_{}_uname'.format(id)]
#         password = request.session['user_{}_upass'.format(id)]
#         if Login.objects.filter(username=username, password=password).exists():
#             tabel = Bookinghotel.objects.filter(
#                 username=username, userpassword=password)
#             hotelurl = '/hotellist/{}/{}'.format('all', id)
#             reviewurl = '/review/{}'.format(id)
#             # this url is for dashboard page itself ....
#             url = "/dashboard/{}".format(id)
#             data = {'un': username, 'pw': password, 'id': id,
#                     'maindata': tabel, 'hotelurl': hotelurl, 'reviewurl': reviewurl, 'url': url}
#             return render(request, 'dashboard.html', data)
#         return render(request, 'dashboard.html', data)


# # this is for order details page..
# def details(request):
#     id = request.GET.get('session__id')
#     if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
#         return HttpResponseRedirect('/login/')
#     elif 'user_{}_uname'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session:
#         data = {}
#         if request.method == "GET":
#             id = request.GET.get('session__id')
#             detail_id = request.GET.get('id1')
#             un = request.session['user_{}_uname'.format(id)]
#             password = request.session['user_{}_upass'.format(id)]

#             url = "/dashboard/{}".format(id)
#             maindata = Bookinghotel.objects.get(id=detail_id)
#             start = str(maindata.start)
#             end = str(maindata.end)
#             res = (dt.strptime(end, "%Y-%m-%d") -
#                    dt.strptime(start, "%Y-%m-%d")).days
#             total_cost = res*maindata.current_cost
#             data = {'un': un, 'pw': password,
#                     'maindata': maindata, 'url': url, 'cost': total_cost, 'id': id}
#             return render(request, 'order_details.html', data)
#         return render(request, 'order_details.html', data)

# # in each page context we have to pass the id value because it is the session key variable so we use this so that we can check if someone is logged in or logged out ...

# # this page is for deleting the order...


# def delete(request):
#     id = request.GET.get('session__id')
#     if 'user_{}_uname'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session:
#         id1 = request.GET.get('id1')
#         id = request.GET.get('session__id')
#         Bookinghotel.objects.filter(id=id1).delete()
#         url = "/dashboard/{}".format(id)
#         return HttpResponseRedirect(url)


# # import all basic rendering and redirecting modules...

# # datetime module is used for deal with dates..

# # this are all our models which we used in this section..

# # we dont required this 2 models here ...
# # from mainapp.models import Login
# # from bookings.models import Bookinghotel


# def hotellist(request, hotelstate, id):
#     if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
#         return HttpResponseRedirect('/login/')

#     elif 'user_{}_uname'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session:
#         user = Login.objects.get(
#             username=request.session.get('user_{}_uname'.format(id)), password=request.session.get('user_{}_upass'.format(id)))
#         username = request.session['user_{}_uname'.format(user.id)]
#         password = request.session['user_{}_upass'.format(user.id)]
#         if Login.objects.filter(username=username, password=password).exists():
#             if hotelstate == "all":
#                 data = Hotellist.objects.all().order_by('?')
#             elif hotelstate == "others":
#                 data = Hotellist.objects.filter(state="gujrat") | Hotellist.objects.filter(
#                     state="laddakh"
#                 ).order_by('?')
#             else:
#                 data = Hotellist.objects.filter(
#                     state=hotelstate).order_by('?')
#             url = "/dashboard/{}".format(id)
#             dash_board_name = username[0:7]
#             datamain = {"un": username, "pw": password,
#                         "url": url, "data": data, 'id': id, 'dn': dash_board_name}
#             return render(request, "hotellist.html", datamain)
#         return render(request, "hotellist.html", datamain)


# # mainapp we created for login details and login model table so here we serve all the pages related to user signup and login..

# # import all basic rendering and redirecting modules...

# # datetime module is used for deal with dates..

# # this are all our models which we used in this section..


# # we dont use Hotellist here..
# # from hotellist.models import Hotellist


# # this is for signup page...
# def signup(request):
#     n = ''
#     cname = ''
#     bool = False
#     data = {'n': n,
#             'bool': bool, 'cname': cname}
#     if request.method == "POST":
#         un = request.POST.get('name')
#         pw = request.POST.get('password')
#         cpw = request.POST.get('cpassword')
#         if pw != cpw:
#             n = "password and confirm password must be same"
#             cname = "alert-danger"
#             bool = 50
#             data = {'n': n,
#                     'bool': bool, 'cname': cname}
#         else:
#             if Login.objects.filter(username=un).exists():
#                 n = "username already exist select another"
#                 cname = "alert-warning"
#                 bool = 40
#                 data = {'n': n,
#                         'bool': bool, 'cname': cname}
#             else:
#                 maindata = Login(username=un, password=pw)
#                 maindata.save()
#                 n = 'You have registerd succesfully! now you can login '
#                 bool = 30
#                 cname = "alert-success"
#                 data = {'n': n,
#                         'bool': bool, 'cname': cname}
#                 hl = "all"
#                 return render(request, 'signup.html', data)
#     return render(request, 'signup.html', data)


# def login(request):

#     if request.method == "GET":
#         n = "for booking you need to login first !"
#         cname = "alert-warning"
#         bool = False
#         data = {'n': n,
#                 'cname': cname,
#                 'bool': bool}
#         return render(request, 'login.html', data)

#     if request.method == "POST":
#         un = request.POST.get('name')
#         pw = request.POST.get('password')
#         if Login.objects.filter(username=un, password=pw).exists():
#             hl = 'all'
#             user = Login.objects.get(username=un, password=pw)
#             request.session['user_{}_uname'.format(user.id)] = un
#             request.session['user_{}_upass'.format(user.id)] = pw
#             id = user.id
#             url = "/hotellist/{}/{}".format(hl, id)
#             return HttpResponseRedirect(url)
#         else:
#             n = "you are not registered create account to login "
#             cname = "alert-danger"
#             bool = 50
#             data = {'n': n,
#                     'cname': cname,
#                     'bool': bool}
#             return render(request, 'login.html', data)
#     return render(request, 'login.html')


# def logout_user(request, id):
#     if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
#         return HttpResponseRedirect('/login/')
#     elif 'user_{}_uname'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session:
#         user = Login.objects.get(
#             username=request.session.get('user_{}_uname'.format(id)))
#         del request.session['user_{}_uname'.format(user.id)]
#         del request.session['user_{}_upass'.format(user.id)]
#         request.session.flush()
#         request.session.clear_expired()
#     return HttpResponseRedirect('/signup/')

# # this is for forgot password and this is before login ...


# def update(request):
#     n = 'enter your new password here'
#     cname = 'alert-warning'
#     bool = False
#     data = {'n': n, 'bool': bool, 'cname': cname}
#     if request.method == "POST":
#         name = request.POST.get('name')
#         new = request.POST.get('newpassword')
#         cnew = request.POST.get('confirm_newpassword')
#         if Login.objects.filter(username=name).exists():
#             main = Login.objects.get(username=name)
#             oldpassword = main.password

#             if new == cnew:
#                 if new == oldpassword:
#                     n = 'your new password is too similar to old password select another !'
#                     cname = 'alert-warning'
#                     bool = 70
#                     data = {'n': n, 'bool': bool, 'cname': cname}
#                 else:
#                     Login.objects.filter(username=name).update(
#                         password=new)
#                     # when we update the password we have to update it in the Bookinghotel table also othewise data is not properly displayed...
#                     Bookinghotel.objects.filter(
#                         username=name).update(userpassword=new)
#                     n = 'your password is updated successfully now you can login !'
#                     cname = 'alert-success'
#                     bool = True
#                     data = {'n': n, 'bool': bool, 'cname': cname}
#             else:
#                 n = 'pasword and confirm password must be same'
#                 cname = 'alert-danger'
#                 bool = 60
#                 data = {'n': n, 'bool': bool, 'cname': cname}
#         else:
#             n = 'No such account is exist'
#             cname = 'alert-danger'
#             bool = 50
#             data = {'n': n, 'bool': bool, 'cname': cname}
#         return render(request, 'update_password.html', data)
#     return render(request, 'update_password.html', data)


# # we can also create one update password after the login .....


# # this views render all tha project level apps which are common to entire project and not required any model query ...
# # this view file is we dont get by default because it is not an application it is the main folder inside our main project this view file I created myself...

# # import all basic rendering and redirecting modules...


# # requests module is used for dealing with api...


# # Create your views here.

# # this 6 are static pages...
# def homepage(request):
#     return render(request, 'index.html')


# def about(request):
#     return render(request, 'about.html')


# def services(request):
#     return render(request, 'services.html')


# def price(request):
#     return HttpResponse('this is price page')


# def staffs(request):
#     return render(request, 'staffs.html')


# def travel(request):
#     data = {}
#     try:
#         if request.method == "POST":
#             id1 = request.POST.get("source")
#             url = "https://trains.p.rapidapi.com/"

#             payload = {"search": id1}
#             headers = {
#                 "content-type": "application/json",
#                 "X-RapidAPI-Key": "a78e10f741mshff5ec54a01b89afp1e0ae3jsnfdbc5239b4a0",
#                 "X-RapidAPI-Host": "trains.p.rapidapi.com",
#             }

#             response = requests.request(
#                 "POST", url, json=payload, headers=headers)
#             datamain = response.json()
#             data = {"datamain": datamain}
#             return render(request, "travel_details.html", data)
#     except Exception as e:
#         pass
#     return render(request, "travel_details.html", data)


# # from here all this are dynamic pages ....

# def homepageid(request, id):
#     if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
#         return HttpResponseRedirect('/')
#     else:
#         url = "/dashboard/{}".format(id)
#         data = {'id': id, 'url': url}
#         return render(request, 'index2.html', data)


# def aboutid(request, id):
#     if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
#         return HttpResponseRedirect('/about/')
#     else:
#         url = "/dashboard/{}".format(id)
#         data = {'id': id, 'url': url}
#         return render(request, 'about2.html', data)


# def servicesid(request, id):
#     if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
#         return HttpResponseRedirect('/services/')
#     else:
#         url = "/dashboard/{}".format(id)
#         data = {'id': id, 'url': url}
#         return render(request, 'services2.html', data)


# def staffsid(request, id):
#     if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
#         return HttpResponseRedirect('/staffs/')
#     else:
#         url = "/dashboard/{}".format(id)
#         data = {'id': id, 'url': url}
#         return render(request, 'staffs2.html', data)


# def travelid(request, id):
#     if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
#         return HttpResponseRedirect('/travel_details/')
#     else:
#         url = "/dashboard/{}".format(id)
#         data = {'id': id, 'url': url}
#         try:
#             if request.method == "POST":
#                 id1 = request.POST.get("source")
#                 url = "https://trains.p.rapidapi.com/"

#                 payload = {"search": id1}
#                 headers = {
#                     "content-type": "application/json",
#                     "X-RapidAPI-Key": "a78e10f741mshff5ec54a01b89afp1e0ae3jsnfdbc5239b4a0",
#                     "X-RapidAPI-Host": "trains.p.rapidapi.com",
#                 }

#                 response = requests.request(
#                     "POST", url, json=payload, headers=headers)
#                 datamain = response.json()
#                 url = "/dashboard/{}".format(id)
#                 data = {"datamain": datamain, 'id': id, 'url': url}
#                 return render(request, "travel_details2.html", data)
#         except Exception as e:
#             pass
#         return render(request, "travel_details2.html", data)


# # this is the feedback form page for users...
# def review(request, id):
#     if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
#         return HttpResponseRedirect('/login/')
#     elif 'user_{}_uname'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session:
#         username = request.session['user_{}_uname'.format(id)]
#         password = request.session['user_{}_upass'.format(id)]
#         n = ''
#         cname = ''
#         bool = False
#         url = "/dashboard/{}".format(id)
#         data = {'un': username, 'n': n,
#                 'cname': cname, 'url': url, 'bool': bool, 'id': id}

#         if request.method == "POST":
#             name = request.POST.get('username')
#             review = request.POST.get('review')
#             ratings = request.POST.get('ratings')
#             data = Review(username=name, user_review=review, ratings=ratings)
#             data.save()
#             n = 'your review is added successfully'
#             cname = 'alert-success'
#             url = "/dashboard/{}".format(id)
#             bool = True
#             data = {'un': username, 'n': n,
#                     'cname': cname, 'url': url, 'bool': bool, 'id': id}

#         return render(request, 'reviewform.html', data)


# # this is the blog page here we display the review of our customers ....
# def blog(request):
#     data = Review.objects.all()
#     datamain = {'data': data}
#     return render(request, 'blogs.html', datamain)


# def blogid(request, id):
#     if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
#         return HttpResponseRedirect('/blogs/')
#     else:
#         data = Review.objects.all()
#         url = "/dashboard/{}".format(id)
#         datamain = {'data': data, 'id': id, 'url': url}
#         return render(request, 'blogs2.html', datamain)









# after this I changed this booking code so that it redirect to the dasbboard page ...

# def bookings(request, id):
#     if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
#         return HttpResponseRedirect('/login/')
#     elif 'user_{}_uname'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session:
#         data = {}
#         data1 = {}
#         bool = False
#         if request.method == "GET":
#             un1 = request.session.get('user_{}_uname'.format(id))
#             password1 = request.session.get('user_{}_upass'.format(id))
#             hname1 = request.GET.get('hname')
#             hcity1 = request.GET.get('hcity')
#             hstate1 = request.GET.get('hstate')
#             hcost1 = request.GET.get('hcost')
#             url = "/dashboard/{}".format(id)
#             data = {'un1': un1, 'pw1': password1, 'hname1': hname1,
#                     'hcity1': hcity1, 'hstate1': hstate1, 'hcost1': hcost1, 'url': url, 'id': id}
#             return render(request, 'booking.html', data)
#         try:
#             if request.method == "POST":
#                 name = request.POST.get('name')
#                 last = request.POST.get('last')
#                 email = request.POST.get('email')
#                 contact = request.POST.get('contact')
#                 person = request.POST.get('person')
#                 # this are hidden fields .....
#                 username = request.POST.get('username')
#                 password = request.POST.get('password')
#                 start = request.POST.get('startdate')
#                 end = request.POST.get('lastdate')
#                 hotelname = request.POST.get('hotelname')
#                 hotelcity = request.POST.get('hotelcity')
#                 hotelstate = request.POST.get('hotelstate')
#                 hotelcost = request.POST.get('hotelcost')

#                 #  this are all the get method variable....
#                 un1 = request.session.get('user_{}_uname'.format(id))
#                 password1 = request.session.get('user_{}_upass'.format(id))
#                 hname1 = request.GET.get('hname')
#                 hcity1 = request.GET.get('hcity')
#                 hstate1 = request.GET.get('hstate')
#                 hcost1 = request.GET.get('hcost')

#                 if end < start:
#                     class_name = 'alert-warning'
#                     bool = 50
#                     n = 'your starting date must be less than ending date'
#                     url = "/dashboard/{}".format(id)
#                     data1 = {'cname': class_name,
#                              'bool': bool,
#                              'n': n, 'un': username, 'pw': password, 'url': url, 'id': id, 'un1': un1, 'pw1': password1, 'hname1': hname1,
#                              'hcity1': hcity1, 'hstate1': hstate1, 'hcost1': hcost1}
                    
#                     return render(request, 'booking.html', data1)
#                 else:
#                     data = Bookinghotel(firstname=name, lastname=last,
#                                         email=email, contact_no=contact, no_people=person, username=username, userpassword=password, start=start, end=end, hotelname=hotelname, city=hotelcity, state=hotelstate, current_cost=hotelcost)
#                     data.save()
                   
#                     class_name = 'alert-success'
#                     bool = True
#                     n = 'your bookings has been done !'
#                     url = url = "/dashboard/{}".format(id)
#                     data1 = {'cname': class_name,
#                              'bool': bool,
#                              'n': n, 'un': username, 'pw': password, 'url': url, 'id': id, 'un1': un1, 'pw1': password1, 'hname1': hname1,
#                              'hcity1': hcity1, 'hstate1': hstate1, 'hcost1': hcost1}
#                     # this is for rendering into the same page ....
#                     # return render(request, 'booking.html', data1)
                    
#                     # this is for redirectin into the daahboard page ...
#                     response=HttpResponseRedirect(url)
#                     messages.success(request, 'your bookings has been done now now you can see the details below !')
#                     return response
                    
#         except Exception as e:
#             pass
#         return render(request, 'booking.html', data1)











# this code does not work but the current version is working may be it is because we dont convert string date to original date ...



# def bookings(request, id):
#     if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
#         return HttpResponseRedirect('/login/')
#     elif 'user_{}_uname'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session:
#         data = {}
#         data1 = {}
#         bool = False
#         if request.method == "GET":
#             un1 = request.session.get('user_{}_uname'.format(id))
#             password1 = request.session.get('user_{}_upass'.format(id))
#             hname1 = request.GET.get('hname')
#             hcity1 = request.GET.get('hcity')
#             hstate1 = request.GET.get('hstate')
#             hcost1 = request.GET.get('hcost')
#             url = "/dashboard/{}".format(id)
#             data = {'un1': un1, 'pw1': password1, 'hname1': hname1,
#                     'hcity1': hcity1, 'hstate1': hstate1, 'hcost1': hcost1, 'url': url, 'id': id}
#             return render(request, 'booking.html', data)
#         try:
#             if request.method == "POST":
#                 name = request.POST.get('name')
#                 last = request.POST.get('last')
#                 email = request.POST.get('email')
#                 contact = request.POST.get('contact')
#                 person = request.POST.get('person')
#                 # this are hidden fields .....
#                 username = request.POST.get('username')
#                 password = request.POST.get('password')
#                 start = request.POST.get('startdate')
#                 end = request.POST.get('lastdate')
#                 hotelname = request.POST.get('hotelname')
#                 hotelcity = request.POST.get('hotelcity')
#                 hotelstate = request.POST.get('hotelstate')
#                 hotelcost = request.POST.get('hotelcost')

#                 #  this are all the get method variable....
#                 un1 = request.session.get('user_{}_uname'.format(id))
#                 password1 = request.session.get('user_{}_upass'.format(id))
#                 hname1 = request.GET.get('hname')
#                 hcity1 = request.GET.get('hcity')
#                 hstate1 = request.GET.get('hstate')
#                 hcost1 = request.GET.get('hcost')

#                 if end < start:
#                     class_name = 'alert-warning'
#                     bool = 50
#                     n = 'your starting date must be less than ending date'
#                     url = "/dashboard/{}".format(id)
#                     data1 = {'cname': class_name,
#                              'bool': bool,
#                              'n': n, 'un': username, 'pw': password, 'url': url, 'id': id, 'un1': un1, 'pw1': password1, 'hname1': hname1,
#                              'hcity1': hcity1, 'hstate1': hstate1, 'hcost1': hcost1}
#                     return render(request, 'booking.html', data1)
#                 else:
#                     data = Bookinghotel(firstname=name, lastname=last,
#                                         email=email, contact_no=contact, no_people=person, username=username, userpassword=password, start=start, end=end, hotelname=hotelname, city=hotelcity, state=hotelstate, current_cost=hotelcost)
#                     data.save()
#                     class_name = 'alert-success'
#                     bool = True
#                     n = 'your bookings has been done now'
#                     url = url = "/dashboard/{}".format(id)
#                     data1 = {'cname': class_name,
#                              'bool': bool,
#                              'n': n, 'un': username, 'pw': password, 'url': url, 'id': id, 'un1': un1, 'pw1': password1, 'hname1': hname1,
#                              'hcity1': hcity1, 'hstate1': hstate1, 'hcost1': hcost1}
#                     return render(request, 'booking.html', data1)
#         except Exception as e:
#             pass
#         return render(request, 'booking.html', data1)