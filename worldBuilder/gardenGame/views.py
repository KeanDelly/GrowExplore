from django.shortcuts import render

# Create your views here.

def mainPage(request):
	return render(request, 'MainPage.html')

def profile(request):
    return render(request, 'profile.html')