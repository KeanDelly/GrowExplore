import datetime
from pyexpat import model
import re
from ssl import AlertDescription
from django.shortcuts import render
from .forms import buildingForm, reportToAdminForm
from django.http import HttpResponseRedirect
from .models import buildingOfTheDay as BOTDModel, reportToAdmin
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.


def mainPage(request):
    building_list = BOTDModel.objects.all()
    if request.user.is_authenticated:
        text = request.user.username
    else:
        text = "error"

    return render(request, 'MainPage.html', {'building_list': building_list , 'today': datetime.date.today, 'user_name': text})

def privacyPolicy(request):
    return render(request, 'privacyPage.html')


def profile(request):
    args = {}

    if request.user.is_authenticated:
        text = request.user.username
    else:
        text = "error"
        return render(request, 'loginError.html')


    user = User.objects.get(username = text)
    streaksTuple = []
    streaksTuple.append(("Harrison Building" ,user.Harrison_Streak))
    streaksTuple.append(("Amory Building" ,user.Amory_Streak))
    streaksTuple.append(("The Forum" ,user.Forum_Streak))
    streaksTuple.append(("Business School Building One" ,user.Business_Streak))
    streaksTuple.append(("Cornwall House Swimming Pool" ,user.Cornwall_Streak))
    streaksTuple.append(("Northcott Theatre" ,user.Northcott_Streak))
    streaksTuple.append(("Geoffrey Pope" ,user.Geoffrey_Streak))
    streaksTuple.append(("Great Hall" ,user.GreatHall_Streak))
    streaksTuple.append(("Hatherly" ,user.Hatherly_Streak))
    streaksTuple.append(("Henry Welcome Building for Biocatalysis" ,user.Henry_Streak))
    streaksTuple.append(("Innovation One | South West Institute of Technology" ,user.Innovation_One_Streak))
    streaksTuple.append(("Institute of Arab and Islamic Studies" ,user.Iais_Streak))
    streaksTuple.append(("INTO International Study Centre" ,user.Into_Streak))
    streaksTuple.append(("Laver" ,user.Laver_Streak))
    streaksTuple.append(("Library" ,user.Library_Streak))
    streaksTuple.append(("Living Systems" ,user.Living_Streak))
    streaksTuple.append(("Mary Harris Memorial Chapel" ,user.Mary_Streak))
    streaksTuple.append(("Old Library" ,user.Old_Library_Streak))
    streaksTuple.append(("Peter Chalk Centre" ,user.Peter_Streak))
    streaksTuple.append(("Physics" ,user.Physics_Streak))
    streaksTuple.append(("Queens" ,user.Queens_Streak))
    streaksTuple.append(("Reed Hall" ,user.Reed_Streak))
    streaksTuple.append(("Reed Mews Wellbeing Centre" ,user.Wellbeing_Streak))
    streaksTuple.append(("Sir Henry Welcome Building for Mood Disorders Research" ,user.Mood_Streak))
    streaksTuple.append(("Sports Park" ,user.Sports_Streak))
    streaksTuple.append(("Streatham Court" ,user.Streatham_Streak))
    streaksTuple.append(("Student Health Centre" ,user.Health_Streak))
    streaksTuple.append(("Washington Singer" ,user.Washington_Streak))
    streaksTuple.append(("Xfi" ,user.Xfi_Streak))
    streaksTuple = sorted(streaksTuple, key=lambda tup: tup[1])
    topStreaks = streaksTuple[-9:]
    topStreaks.reverse()
    topStreaks1Name = topStreaks[0][0]
    topStreaks1Number = str(topStreaks[0][1])
    topStreaks2Name = topStreaks[1][0]
    topStreaks2Number = str(topStreaks[1][1])
    topStreaks3Name = topStreaks[2][0]
    topStreaks3Number = str(topStreaks[2][1])
    topStreaks4Name = topStreaks[3][0]
    topStreaks4Number = str(topStreaks[3][1])
    topStreaks5Name = topStreaks[4][0]
    topStreaks5Number = str(topStreaks[4][1])
    topStreaks6Name = topStreaks[5][0]
    topStreaks6Number = str(topStreaks[5][1])
    topStreaks7Name = topStreaks[6][0]
    topStreaks7Number = str(topStreaks[6][1])
    topStreaks8Name = topStreaks[7][0]
    topStreaks8Number = str(topStreaks[7][1])
    topStreaks9Name = topStreaks[8][0]
    topStreaks9Number = str(topStreaks[8][1])
    args={'user_name': text, 'topStreaks1Name': topStreaks1Name, 'topStreaks1Number':topStreaks1Number,  'topStreaks2Name': topStreaks2Name, 'topStreaks2Number':topStreaks2Number, 'topStreaks3Name': topStreaks3Name, 'topStreaks3Number':topStreaks3Number, 'topStreaks4Name': topStreaks4Name, 'topStreaks4Number':topStreaks4Number, 'topStreaks5Name': topStreaks5Name, 'topStreaks5Number':topStreaks5Number, 'topStreaks6Name': topStreaks6Name, 'topStreaks6Number':topStreaks6Number, 'topStreaks7Name': topStreaks7Name, 'topStreaks7Number':topStreaks7Number, 'topStreaks8Name': topStreaks8Name, 'topStreaks8Number':topStreaks8Number, 'topStreaks9Name': topStreaks9Name, 'topStreaks9Number':topStreaks9Number }

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
                print("ERROR")
                return HttpResponseRedirect('/main/buildingOfTheDay?submitted=False')
            form.save()
        return HttpResponseRedirect('/main/buildingOfTheDay?submitted=True')
    else:
        form = buildingForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'buildingOfTheDay.html', {"form": form, 'submitted': submitted, 'building_list': building_list})



def reportToAdmin(request):
    submitted = False
    if request.method == "POST":
        form = reportToAdminForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/main/reportToAdmin?submitted=True')
    else:
        form = reportToAdminForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'reportToAdmin.html', {"form": form, 'submitted': submitted})