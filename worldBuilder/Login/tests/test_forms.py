from django.test import TestCase
#import forms.py
from Login.forms import NewUserForm
import datetime

class TestForm(TestCase):
    #Base Tests from Before Staff Verification
    def test_NewUserForm_no_data(self):
        form = NewUserForm(data={})
        self.assertFalse(form.is_valid())
    def test_NewUserForm_good_data(self):
        form = NewUserForm(data = {"username":'Name1', "email":'email1@gmail.com',"password1" : 'Campus123', "password2":'Campus123'})
        self.assertTrue(form.is_valid())
    def test_NewUserForm_bad_data(self):
        form = NewUserForm(data = {"username":'Name1', "email":'email1@gmail.com',"password1" : '12345', "password2":'12345'})
        self.assertFalse(form.is_valid())

    #Tests for Staff Verification
    def test_StaffUserForm_no_data(self):
        form = NewUserForm(data={})
        self.assertFalse(form.is_valid())
    def test_StaffUserForm_good_data(self):
        form = NewUserForm(data = {"username":'Name1', "email":'email1@gmail.com',"password1" : 'Campus123', "password2":'Campus123', "staffVerification":"54321"})
        self.assertTrue(form.is_valid())
    def test_StaffUserForm_good_data_blank(self):
        form = NewUserForm(data = {"username":'Name1', "email":'email1@gmail.com',"password1" : 'Campus123', "password2":'Campus123', "staffVerification":""})
        self.assertTrue(form.is_valid())
    def test_StaffUserForm_bad_data(self):
        form = NewUserForm(data = {"username":'Name1', "email":'email1@gmail.com',"password1" : '12345', "password2":'12345'})
        self.assertFalse(form.is_valid())