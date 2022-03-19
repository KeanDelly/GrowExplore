from django.test import TestCase
#import forms.py
from gardenGame.forms import buildingForm, reportToAdminForm
import datetime

class TestForm(TestCase):
    def test_building_form_no_data(self):
        form = buildingForm(data={})
        self.assertFalse(form.is_valid())
    def test_building_form_good_data(self):
        form = buildingForm(data = {'name':'Name1', 'description':'Description1','date': datetime.date(2022, 3,19), 'reward':'reward1'})
        self.assertTrue(form.is_valid())
    def test_report_to_admin_form_no_data(self):
        form = reportToAdminForm(data = {})
        self.assertFalse(form.is_valid())
    def test_report_to_admin_form_good_data(self):
        form = reportToAdminForm(data = {'problem_name':'ProblemName1', 'problem_description':'ProblemDescription1', 'username':'Name1', 'email':'Email1@gmail.com'})
        self.assertTrue(form.is_valid())