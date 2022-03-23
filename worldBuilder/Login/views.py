from django.shortcuts import render
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import get_user_model
User = get_user_model()
from datetime import datetime
import re
from gardenGame.models import buildingOfTheDay

from pathlib import Path
import os
from datetime import date
from django.http import HttpResponse




DIR = Path(__file__).resolve().parent.parent

directory = "static/Users/"

BASE_DIR = os.path.join(DIR, directory)

building_list = ["Harrison Building","Amory Building","The Forum",
				 "Business School Building One","Cornwall House",
				 "Northcott Theatre","Geoffrey Pope","Great Hall","Hatherly",
				 "Henry Wellcome | Biocatalysis",
				 "Innovation One SWIoT",
				 "Institute of AIS","INTO Study Centre",
                 "Laver","Living Systems","Mary Harris","Old Library",
                 "Peter Chalk Centre","Physics","Queens","Reed Hall","Reed Mews Wellbeing Centre",
                 "Sir Henry Wellcome Building","Sports Park",
                 "Streatham Court","Student Health Centre","Washington Singer","Xfi"]


# Create your views here.


def homepage(request):
	return render(request, 'homepage.html')


def login_error(request):
	return render(request, 'loginError.html')


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")

				today = date.today()
				d1 = today.strftime("%d/%m/%Y")
				current_date = d1.split("/")
				#read in that users file and store it as array
				#increment the login one, update the date
				#then write the whole file back

				file_contents_array = []
				with open(os.path.join(BASE_DIR, username + ".txt")) as my_file:
					for line in my_file:
						file_contents_array.append(line)

				my_file.close()

				login_holder = file_contents_array[0]

				login_data = login_holder.split(",")

				last_logged_date = login_data[2]
				last_logged_date = last_logged_date.split("/")

				if (last_logged_date[0] < current_date[0]):
					login_data[1] = str(int(login_data[1]) + 1)
					login_data[2] = d1
				elif (last_logged_date[1] < current_date[1]):
					login_data[1] = str(int(login_data[1]) + 1)
					login_data[2] = d1
				elif (last_logged_date[2] < current_date[2]):
					login_data[1] = str(int(login_data[1]) + 1)
					login_data[2] = d1

				login_holder = ','.join(login_data)

				file_contents_array[0] = login_holder+"\n"

				fileOverwrite = open(os.path.join(BASE_DIR, form.cleaned_data['username'] + ".txt"), "w")

				for line in file_contents_array:
					fileOverwrite.write(line)

				fileOverwrite.close()

				return redirect('/main/')
			else:
				messages.error(request, "Invalid username or password.")
				return redirect('/loginError')
		else:
			messages.error(request, "Invalid username or password.")
			return redirect('/loginError')
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			code = form.cleaned_data.get('staffVerification')
			user = User(username=form.cleaned_data.get('username'), email =form.cleaned_data.get('email') )
			user.set_password(form.cleaned_data.get('password1'))
			if code != "":
				if code == "54321":
					user.is_superuser=True
					user.is_staff=True
				else:
					messages.error(request, "Unsuccessful registration, Invalid Staff Code")
					return redirect('/loginError')

			user.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			today = date.today()
			d1 = today.strftime("%d/%m/%Y")
			current_date = d1.split("/")
			current_date[0] = str(int(current_date[0])-1)
			fileCreate = open(os.path.join(BASE_DIR, form.cleaned_data['username']+".txt"), "x")
			fileCreate.write("login_streak,0,"+current_date[0]+"/"+current_date[1]+"/"+current_date[2])
			fileCreate.close()
			fileAppend = open(os.path.join(BASE_DIR, form.cleaned_data['username']+".txt"), "a")
			for build in building_list:
				fileAppend.write(build + ",0,00/00/0000\n")
			fileCreate.close()
			return redirect('/main')
		messages.error(request, "Unsuccessful registration. Invalid information.")
		return redirect('/loginError')
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def loginStreak(request, user_id):
    user = User.objects.get(id=user_id)
    if(user.LastLogin != datatime.today()):
        user.LoginStreak = user.LoginStreak+1
        user.LastLogin = datetime.now().date()
    user.save()
    redirect("/main")

def simple_function(request):
    listTemp = str(request).split("?")
    TempUsername = request.user.username

    Temp = listTemp[1]
    Temp = Temp.split("%20&%20")[0]
    building = re.sub(r'%20', ' ', Temp)
    building = re.sub(r"'>", '', building)
    building = re.sub(r'You%20have%20checked%20in%20at%20:%20','',building)

    ##May need to correct string to be int and then put in error handing
    userList = User.objects.get(username = TempUsername)
    user = userList
    if(building == "Harrison Building"):
        if(str(user.Harrison_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Harrison_Streak = user.Harrison_Streak + 1
            user.Harrison_lastLogin = datetime.now().date()

    elif(building == "Amory Building"):
        if(str(user.Amory_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Amory_Streak = user.Amory_Streak + 1
            user.Amory_lastLogin = datetime.now().date()

    elif(building == "The Forum"):
        if(str(user.Forum_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Forum_Streak = user.Forum_Streak + 1
            user.Forum_lastLogin = datetime.now().date()

    elif(building == "Business School Building One"):
        if(str(user.Business_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Business_Streak = user.Business_Streak + 1
            user.Business_lastLogin = datetime.now().date()

    elif(building == "Cornwall House Swimming Pool"):
        if(str(user.Cornwall_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Cornwall_Streak = user.Cornwall_Streak + 1
            user.Cornwall_lastLogin = datetime.now().date()

    elif(building == "Northcott Theatre"):
        if(str(user.Northcott_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Northcott_Streak = user.Northcott_Streak + 1
            user.Northcott_lastLogin = datetime.now().date()

    elif(building == "Geoffrey Pope"):
        if(str(user.Geoffrey_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Geoffrey_Streak = user.Geoffrey_Streak + 1
            user.Geoffrey_lastLogin = datetime.now().date()

    elif(building == "Great Hall"):
        if(str(user.GreatHall_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.GreatHall_Streak = user.GreatHall_Streak + 1
            user.GreatHall_lastLogin = datetime.now().date()

    elif(building == "Hatherly"):
        if(str(user.Hatherly_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Hatherly_Streak = user.Hatherly_Streak + 1
            user.Hatherly_lastLogin = datetime.now().date()

    elif(building == "Henry Welcome Building for Biocatalysis"):
        if(str(user.Henry_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Henry_Streak = user.Henry_Streak + 1
            user.Henry_lastLogin = datetime.now().date()

    elif(building == "Innovation One | South West Institute of Technology"):
        if(str(user.Innovation_One_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Innovation_One_Streak = user.Innovation_One_Streak + 1
            user.Innovation_One_lastLogin = datetime.now().date()

    elif(building == "Institute of Arab and Islamic Studies"):
        if(str(user.Iais_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Iais_Streak = user.Iais_Streak + 1
            user.Iais_lastLogin = datetime.now().date()

    elif(building == "INTO International Study Centre"):
        if(str(user.into_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Into_Streak = user.Into_Streak + 1
            user.into_lastLogin = datetime.now().date()

    elif(building == "Laver"):
        if(str(user.Laver_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Laver_Streak = user.Laver_Streak + 1
            user.Laver_lastLogin = datetime.now().date()

    elif(building == "Library"):
        if(str(user.Library_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Library_Streak = user.Library_Streak + 1
            user.Library_lastLogin = datetime.now().date()

    elif(building == "Living Systems"):
        if(str(user.Living_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Living_Streak = user.Living_Streak + 1
            user.Living_lastLogin = datetime.now().date()

    elif(building == "Mary Harris Memorial Chapel"):
        if(str(user.Mary_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Mary_Streak = user.Mary_Streak + 1
            user.Mary_lastLogin = datetime.now().date()

    elif(building == "Old Library"):
        if(str(user.Old_Library_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Old_Library_Streak = user.Old_Library_Streak + 1
            user.Old_Library_lastLogin = datetime.now().date()

    elif(building == "Peter Chalk Centre"):
        if(str(user.Peter_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Peter_Streak = user.Peter_Streak + 1
            user.Peter_lastLogin = datetime.now().date()

    elif(building == "Physics"):
        if(str(user.Physics_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Physics_Streak = user.Physics_Streak + 1
            user.Physics_lastLogin = datetime.now().date()

    elif(building == "Queens"):
        if(str(user.Queen_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Queens_Streak = user.Queens_Streak + 1
            user.Queen_lastLogin = datetime.now().date()

    elif(building == "Reed Hall"):
        if(str(user.Reed_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Reed_Streak = user.Reed_Streak + 1
            user.Reed_lastLogin = datetime.now().date()

    elif(building == "Reed Mews Wellbeing Centre"):
        if(str(user.Wellbeing_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Wellbeing_Streak = user.Wellbeing_Streak + 1
            user.Wellbeing_lastLogin = datetime.now().date()

    elif(building == "Sir Henry Welcome Building for Mood Disorders Research"):
        if(str(user.Mood_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Mood_Streak = user.Mood_Streak + 1
            user.Mood_lastLogin = datetime.now().date()

    elif(building == "Sports Park"):
        if(str(user.Sports_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Sports_Streak = user.Sports_Streak + 1
            user.Sports_lastLogin = datetime.now().date()

    elif(building == "Streatham Court"):
        if(str(user.Streatham_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Streatham_Streak = user.Streatham_Streak + 1
            user.Streatham_lastLogin = datetime.now().date()

    elif(building == "Student Health Centre"):
        if(str(user.Health_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Health_Streak = user.Health_Streak + 1
            user.Health_lastLogin = datetime.now().date()

    elif(building == "Washington Singer"):
        if(str(user.Washington_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Washington_Streak = user.Washington_Streak + 1
            user.Washington_lastLogin = datetime.now().date()

    elif(building == "Xfi"):
        if(str(user.Xfi_lastLogin) != str(datetime.today().strftime('%Y-%m-%d'))):
            user.Xfi_Streak = user.Xfi_Streak + 1
            user.Xfi_lastLogin = datetime.now().date()


    buildingsOTDList = buildingOfTheDay.objects.all()
    buildingOTD = None
    for i in buildingsOTDList:
        if(str(i.date) == datetime.today().strftime('%Y-%m-%d')):
            buildingOTD = i
    if(buildingOTD.name == building):
        reward = buildingOTD.reward
        if(user.UserRewards != ""):
            user.UserRewards = user.UserRewards + "*" + reward
        else:
            user.UserRewards = reward
    user.save()
    return redirect("/main")

def test(request):

	if request.GET.get('NameOfYourButton') == 'YourValue':
		print('\nuser')
		print('\nuser clicked button')
		return HttpResponse("""<html><script>window.location.replace('/')</script></html>""")



