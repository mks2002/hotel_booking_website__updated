
# this views render all tha project level apps which are common to entire project and not required any model query ...
# this view file is we dont get by default because it is not an application it is the main folder inside our main project this view file I created myself...


# import all basic rendering and redirecting modules...
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# requests module is used for dealing with api...
import requests


# Create your views here.

# this 6 are static pages...
def homepage(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def price(request):
    return HttpResponse('this is price page')


def staffs(request):
    return render(request, 'staffs.html')


def travel(request):
    data = {}
    try:
        if request.method == "POST":
            id1 = request.POST.get("source")
            url = "https://trains.p.rapidapi.com/"

            payload = {"search": id1}
            headers = {
                "content-type": "application/json",
                "X-RapidAPI-Key": "a78e10f741mshff5ec54a01b89afp1e0ae3jsnfdbc5239b4a0",
                "X-RapidAPI-Host": "trains.p.rapidapi.com",
            }

            response = requests.request(
                "POST", url, json=payload, headers=headers)
            datamain = response.json()
            data = {"datamain": datamain}
            return render(request, "travel_details.html", data)
    except Exception as e:
        pass
    return render(request, "travel_details.html", data)


# from here all this are dynamic pages ....

def homepageid(request, id):
    if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
        return HttpResponseRedirect('/login/')
    else:
        url = "/dashboard/{}".format(id)
        data = {'id': id, 'url': url}
        return render(request, 'index2.html', data)


def aboutid(request, id):
    if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
        return HttpResponseRedirect('/login/')
    else:
        url = "/dashboard/{}".format(id)
        data = {'id': id, 'url': url}
        return render(request, 'about2.html', data)


def servicesid(request, id):
    if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
        return HttpResponseRedirect('/login/')
    else:
        url = "/dashboard/{}".format(id)
        data = {'id': id, 'url': url}
        return render(request, 'services2.html', data)


def staffsid(request, id):
    if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
        return HttpResponseRedirect('/login/')
    else:
        url = "/dashboard/{}".format(id)
        data = {'id': id, 'url': url}
        return render(request, 'staffs2.html', data)


def travelid(request, id):
    if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session:
        return HttpResponseRedirect('/login/')
    else:
        url = "/dashboard/{}".format(id)
        data = {'id': id, 'url': url}
        try:
            if request.method == "POST":
                id1 = request.POST.get("source")
                url = "https://trains.p.rapidapi.com/"

                payload = {"search": id1}
                headers = {
                    "content-type": "application/json",
                    "X-RapidAPI-Key": "a78e10f741mshff5ec54a01b89afp1e0ae3jsnfdbc5239b4a0",
                    "X-RapidAPI-Host": "trains.p.rapidapi.com",
                }

                response = requests.request(
                    "POST", url, json=payload, headers=headers)
                datamain = response.json()
                url = "/dashboard/{}".format(id)
                data = {"datamain": datamain, 'id': id, 'url': url}
                return render(request, "travel_details2.html", data)
        except Exception as e:
            pass
        return render(request, "travel_details2.html", data)
