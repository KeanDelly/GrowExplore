from django.test import TestCase, Client
##from django.urls import reverse
##from budget.models import Project, Category, Expense
import json

class TestViews(TestCase):
    def test_mainPage_GET(self):
       client = Client()
       response = client.get('/main/')
       self.assertEquals(response.status_code, 200)
       self.assertTemplateUsed(response, 'MainPage.html')

    def test_profilePage_GET(self):
        client = Client()
        response = client.get('/main/profile/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_buildingOfTheDayPage_GET(self):
        client = Client()
        response = client.get('/main/buildingOfTheDay/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'buildingOfTheDay.html')

