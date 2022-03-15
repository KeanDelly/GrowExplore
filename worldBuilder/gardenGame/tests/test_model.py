from django.test import TestCase
from .models import buildingOfTheDay


class TestModels(TestCase):

    def setUp(self) -> None:
        buildingOfTheDay.objects.create()

    """These tests check that the model has the right label to the user"""

    def test_building_name_label(self):
        building = buildingOfTheDay.objects.get(id=1)
        field_label = building._meta.get_field('building_name').verbose_name
        self.assertEqual(field_label, 'Building Name')

    def test_building_description_label(self):
        building = buildingOfTheDay.objects.get(id=1)
        field_label = building._meta.get_field('building_desc').verbose_name
        self.assertEqual(field_label, 'Building Description')

    def test_date_label(self):
        building = buildingOfTheDay.objects.get(id=1)
        field_label = building._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'Date')

    def test_reward_label(self):
        building = buildingOfTheDay.objects.get(id=1)
        field_label = building._meta.get_field('reward').verbose_name
        self.assertEqual(field_label, 'reward')
