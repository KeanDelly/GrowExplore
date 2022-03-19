from django.test import TestCase
#import forms.py
from gardenGame.forms import buildingForm


class TestForms(TestCase):
    def test_building_form_no_data(self):
        form = buildingForm(data={})
        self.assertFalse(form.is_valid())
