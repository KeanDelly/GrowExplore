from django.test import TestCase, Client


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
        self.assertTemplateUsed(response, 'loginError.html')

    def test_buildingOfTheDayPage_GET(self):
        client = Client()
        response = client.get('/main/buildingOfTheDay/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'buildingOfTheDay.html')

    def test_reportToAdmin_GET(self):
        client = Client()
        response = client.get('/main/reportToAdmin/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'reportToAdmin.html')

    def test_privacyPolicy_GET(self):
        client = Client()
        response = client.get('/main/privacyPolicy/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'privacyPage.html')
