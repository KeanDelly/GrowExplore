from django.test import TestCase

class URLTests(TestCase):
    def test_testLogin(self):
        response = self.client.get('/') ## gets a response from the server and stores it
        self.assertEqual(response.status_code, 200) ## checks if it worked, for the homepage
        response = self.client.get('/login/') ## gets a response from the server and stores it
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/register/') ## gets a response from the server and stores it
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/loginError/') ## gets a response from the server and stores it
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/password_reset/') ## gets a response from the server and stores it
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/password_reset_sent/') ## gets a response from the server and stores it
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/reset/done/') ## gets a response from the server and stores it
        self.assertEqual(response.status_code, 200)

## this will test that the URL is all set up and you get the correct response when you ping the server
