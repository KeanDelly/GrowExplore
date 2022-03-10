import datetime
from pyexpat import model
import re
from ssl import AlertDescription
from django.shortcuts import render
from .forms import buildingForm
from django.http import HttpResponseRedirect
from .models import buildingOfTheDay as BOTDModel

# Create your views here.


def mainPage(request):
    building_list = BOTDModel.objects.all()
    return render(request, 'MainPage.html', {'building_list': building_list , 'today': datetime.date.today})


def profile(request):
    args = {}

    if request.user.is_authenticated:
        text = request.user.username
    else:
        text = "error"

    args['user_name'] = text
    return render(request, 'profile.html', args)


def buildingOfTheDay(request):
    submitted = False
    building_list = BOTDModel.objects.all()
    if request.method == "POST":
        form = buildingForm(request.POST)
        if form.is_valid():
            building_dates = BOTDModel.objects.filter(
                date=form.cleaned_data['date'])
            if len(building_dates) != 0:

                return HttpResponseRedirect('/main/buildingOfTheDay?submitted=False')
            form.save()
        return HttpResponseRedirect('/main/buildingOfTheDay?submitted=True')
    else:
        form = buildingForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'buildingOfTheDay.html', {"form": form, 'submitted': submitted, 'building_list': building_list})
