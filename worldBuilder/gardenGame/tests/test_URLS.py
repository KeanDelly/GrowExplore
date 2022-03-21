from django.test import TestCase


class URLTests(TestCase):

    def test_GardenGame(self):
        response = self.client.get('/main/') ## gets a response from the server and stores it
        self.assertEqual(response.status_code, 200) ## checks if it worked
        response = self.client.get('/main/profile/') ## gets a response from the server and stores it
        self.assertEqual(response.status_code, 200) ## checks if it worked
        response = self.client.get('/main/buildingOfTheDay/') ## gets a response from the server and stores it
        self.assertEqual(response.status_code, 200)  ## checks if it worked
        response = self.client.get('/main/reportToAdmin/')  ## gets a response from the server and stores it
        self.assertEqual(response.status_code, 200)  ## checks if it worked
        response = self.client.get('/main/privacyPolicy/')  ## gets a response from the server and stores it
        self.assertEqual(response.status_code, 200)  ## checks if it worked

## this will test that the URL is all set up and you get the correct response when you ping the server

