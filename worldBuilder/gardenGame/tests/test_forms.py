from django.test import TestCase
import forms.py


class TestForms(TestCase):

    def test_building_form_no_data(self):
        form = forms.buildingForm(data={})
        self.assertFalse(form.is_valid())
