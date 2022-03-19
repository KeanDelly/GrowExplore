from django.test import TestCase
#import forms.py
from Login.forms import NewUserForm
import datetime

class TestForm(TestCase):
    def test_NewUserForm_no_data(self):
        form = NewUserForm(data={})
        self.assertFalse(form.is_valid())
    def test_NewUserForm_good_data(self):
        form = NewUserForm(data = {"username":'Name1', "email":'email1@gmail.com',"password1" : 'Campus123', "password2":'Campus123'})
        self.assertTrue(form.is_valid())
    def test_NewUserForm_bad_data(self):
        form = NewUserForm(data = {"username":'Name1', "email":'email1@gmail.com',"password1" : '12345', "password2":'12345'})
        self.assertFalse(form.is_valid())