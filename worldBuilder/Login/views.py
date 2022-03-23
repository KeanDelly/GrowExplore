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
			return redirect('/main')
		messages.error(request, "Unsuccessful registration. Invalid information.")
		return redirect('/loginError')
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def loginStreak(request, user_id):
    user = User.objects.get(id=user_id)
    if(user.LastLogin != datatime.today()):
        user.LoginStreak = user.LoginStreak+1
        user.LastLogin = datetime.today()
    user.save()
    redirect("/main")

def simple_function(request):
    listTemp = str(request).split("?")
    TempUsername = listTemp[2]

    Temp = listTemp[1]
    Temp = Temp.split("%20&%20")[0]
    building = re.sub(r'%20', ' ', Temp)
    building = re.sub(r"'>", '', building)
    building = re.sub(r'You%20have%20checked%20in%20at%20:%20','',building)

    ##May need to correct string to be int and then put in error handing
    userList = User.objects.get(username = TempUsername)
    user = userList
    if(building == "Harrison Building"):
        if(user.Harrison_lastLogin != str(datetime.today())):
            user.Harrison_Streak = user.Harrison_Streak + 1
            user.Harrison_lastLogin = datetime.today()

    elif(building == "Amory Building"):
        if(user.Amory_lastLogin != str(datetime.today())):
            user.Amory_Streak = user.Amory_Streak + 1
            user.Amory_lastLogin = datetime.today()

    elif(building == "The Forum"):
        if(user.Forum_lastLogin != str(datetime.today())):
            user.Forum_Streak = user.Forum_Streak + 1
            user.Forum_lastLogin = datetime.today()

    elif(building == "Business School Building One"):
        if(user.Business_lastLogin != str(datetime.today())):
            user.Business_Streak = user.Business_Streak + 1
            user.Business_lastLogin = datetime.today()

    elif(building == "Cornwall House Swimming Pool"):
        if(user.Cornwall_lastLogin != str(datetime.today())):
            user.Cornwall_Streak = user.Cornwall_Streak + 1
            user.Cornwall_lastLogin = datetime.today()

    elif(building == "Northcott Theatre"):
        if(user.Northcott_lastLogin != str(datetime.today())):
            user.Northcott_Streak = user.Northcott_Streak + 1
            user.Northcott_lastLogin = datetime.today()

    elif(building == "Geoffrey Pope"):
        if(user.Geoffrey_lastLogin != str(datetime.today())):
            user.Geoffrey_Streak = user.Geoffrey_Streak + 1
            user.Geoffrey_lastLogin = datetime.today()

    elif(building == "Great Hall"):
        if(user.GreatHall_lastLogin != str(datetime.today())):
            user.GreatHall_Streak = user.GreatHall_Streak + 1
            user.GreatHall_lastLogin = datetime.today()

    elif(building == "Hatherly"):
        if(user.Hatherly_lastLogin != str(datetime.today())):
            user.Hatherly_Streak = user.Hatherly_Streak + 1
            user.Hatherly_lastLogin = datetime.today()

    elif(building == "Henry Welcome Building for Biocatalysis"):
        if(user.Henry_lastLogin != str(datetime.today())):
            user.Henry_Streak = user.Henry_Streak + 1
            user.Henry_lastLogin = datetime.today()

    elif(building == "Innovation One | South West Institute of Technology"):
        if(user.Innovation_One_lastLogin != str(datetime.today())):
            user.Innovation_One_Streak = user.Innovation_One_Streak + 1
            user.Innovation_One_lastLogin = datetime.today()

    elif(building == "Institute of Arab and Islamic Studies"):
        if(user.Iais_lastLogin != str(datetime.today())):
            user.Iais_Streak = user.Iais_Streak + 1
            user.Iais_lastLogin = datetime.today()

    elif(building == "INTO International Study Centre"):
        if(user.into_lastLogin != str(datetime.today())):
            user.Into_Streak = user.Into_Streak + 1
            user.into_lastLogin = datetime.today()

    elif(building == "Laver"):
        if(user.Laver_lastLogin != str(datetime.today())):
            user.Laver_Streak = user.Laver_Streak + 1
            user.Laver_lastLogin = datetime.today()

    elif(building == "Library"):
        if(user.Library_lastLogin != str(datetime.today())):
            user.Library_Streak = user.Library_Streak + 1
            user.Library_lastLogin = datetime.today()

    elif(building == "Living Systems"):
        if(user.Living_lastLogin != str(datetime.today())):
            user.Living_Streak = user.Living_Streak + 1
            user.Living_lastLogin = datetime.today()

    elif(building == "Mary Harris Memorial Chapel"):
        if(user.Mary_lastLogin != str(datetime.today())):
            user.Mary_Streak = user.Mary_Streak + 1
            user.Mary_lastLogin = datetime.today()

    elif(building == "Old Library"):
        if(user.Old_Library_lastLogin != str(datetime.today())):
            user.Old_Library_Streak = user.Old_Library_Streak + 1
            user.Old_Library_lastLogin = datetime.today()

    elif(building == "Peter Chalk Centre"):
        if(user.Peter_lastLogin != str(datetime.today())):
            user.Peter_Streak = user.Peter_Streak + 1
            user.Peter_lastLogin = datetime.today()

    elif(building == "Physics"):
        if(user.Physics_lastLogin != str(datetime.today())):
            user.Physics_Streak = user.Physics_Streak + 1
            user.Physics_lastLogin = datetime.today()

    elif(building == "Queens"):
        if(user.Queen_lastLogin != str(datetime.today())):
            user.Queens_Streak = user.Queens_Streak + 1
            user.Queen_lastLogin = datetime.today()

    elif(building == "Reed Hall"):
        if(user.Reed_lastLogin != str(datetime.today())):
            user.Reed_Streak = user.Reed_Streak + 1
            user.Reed_lastLogin = datetime.today()

    elif(building == "Reed Mews Wellbeing Centre"):
        if(user.Wellbeing_lastLogin != str(datetime.today())):
            user.Wellbeing_Streak = user.Wellbeing_Streak + 1
            user.Wellbeing_lastLogin = datetime.today()

    elif(building == "Sir Henry Welcome Building for Mood Disorders Research"):
        if(user.Mood_lastLogin != str(datetime.today())):
            user.Mood_Streak = user.Mood_Streak + 1
            user.Mood_lastLogin = datetime.today()

    elif(building == "Sports Park"):
        if(user.Sports_lastLogin != str(datetime.today())):
            user.Sports_Streak = user.Sports_Streak + 1
            user.Sports_lastLogin = datetime.today()

    elif(building == "Streatham Court"):
        if(user.Streatham_lastLogin != str(datetime.today())):
            user.Streatham_Streak = user.Streatham_Streak + 1
            user.Streatham_lastLogin = datetime.today()

    elif(building == "Student Health Centre"):
        if(user.Health_lastLogin != str(datetime.today())):
            user.Health_Streak = user.Health_Streak + 1
            user.Health_lastLogin = datetime.today()

    elif(building == "Washington Singer"):
        if(user.Washington_lastLogin != str(datetime.today())):
            user.Washington_Streak = user.Washington_Streak + 1
            user.Washington_lastLogin = datetime.today()

    elif(building == "Xfi"):
        if(user.Xfi_lastLogin != str(datetime.today())):
            user.Xfi_Streak = user.Xfi_Streak + 1
            user.Xfi_lastLogin = datetime.today()


    buildingOTD = buildingOfTheDay.objects.get(name = building)
    if(buildingOTD == building):
        reward = buildingOTD.reward
        if(user.UserRewards != ""):
            user.UserRewards = user.userRewards + "*" + reward
        else:
            user.UserRewards = reward
    user.save()
    return redirect("/main")


