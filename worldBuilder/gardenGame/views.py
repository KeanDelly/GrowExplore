from django.shortcuts import render

# Create your views here.

def mainPage(request):
	return render(request, 'MainPage.html')

def profile(request):
    args = {}

    if request.user.is_authenticated:
        text = request.user.username
    else:
        text = "error"

    args['user_name'] = text
    return render(request, 'profile.html', args)