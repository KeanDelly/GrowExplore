from django.test import TestCase

class URLTests(TestCase):
    def test_testLogin(self):
        response = self.client.get('/') ## gets a response from the server and stores it
        self.assertEqual(response.status_code, 200) ## checks if it worked, for the homepage
        response = self.client.get('/login/') ## gets a response from the server and stores it
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/register/') ## gets a response from the server and stores it
        self.assertEqual(response.status_code, 200)

## this will test that the URL is all set up and you get the correct response when you ping the server