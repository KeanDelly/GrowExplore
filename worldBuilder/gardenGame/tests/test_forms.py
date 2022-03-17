from django.test import TestCase
import sys
sys.path.insert(0, '/worldBuilder/gardenGame/forms/')
from forms import buildingForm

class TestForms(TestCase):

    def test_building_form_no_data(self):
        form = buildingForm(data={})
        self.assertFalse(form.is_valid())
