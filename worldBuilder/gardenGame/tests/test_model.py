from django.test import TestCase
from gardenGame.models import buildingOfTheDay, reportToAdmin

import datetime

class TestBuildingOfTheDay(TestCase):

    def setUp(self) -> None:  ##Sets up basic correct object in test database
        buildingOfTheDay.objects.create(
            name = 'Name1',
            description = 'Description1',
            date = datetime.date(2022,3,19),
            reward = 'Reward1'
        )

    """These tests check that the model has the right label to the user"""

    def test_building_name_label(self):
        building = buildingOfTheDay.objects.get(id=1)
        field_label = building._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')



    def test_building_description_label(self):
        building = buildingOfTheDay.objects.get(id=1)
        field_label = building._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_date_label(self):
        building = buildingOfTheDay.objects.get(id=1)
        field_label = building._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_reward_label(self):
        building = buildingOfTheDay.objects.get(id=1)
        field_label = building._meta.get_field('reward').verbose_name
        self.assertEqual(field_label, 'reward')

    def testInputtingDataCorrectly(self):
        building = buildingOfTheDay.objects.get(id = 1)
        self.assertEqual(building.name, 'Name1')
        self.assertEqual(building.description, 'Description1')
        self.assertEqual(building.date, datetime.date(2022,3,19))
        self.assertEqual(building.reward, 'Reward1')

class TestReportToAdmin(TestCase):
    def setUp(self):
        self.testInput = reportToAdmin.objects.create(
           problem_name = 'Probelm1',
           problem_description = 'Description1',
           username = 'username1',
           email = 'email1@gmail.com'
        )
    def TestLabels(self):  ##These check the label names of the field attributes, this is really testing if the attributes we created are all there and correct
        self.assertEqual(testInput._meta.get_field('problem_name').verbose_name, 'problem_name')
        self.assertEqual(testInput._meta.get_field('description').verbose_name, 'description')
        self.assertEqual(testInput._meta.get_field('username').verbose_name, 'username')
        self.assertEqual(testInput._meta.get_field('email').verbose_name, 'email')
    def TestInputtingDataCorrectly(self): ##These take a false input to the model and check it all works
        self.assertEqual(testInput.problem_name, 'Probelm1')
        self.assertEqual(testInput.problem_description, 'Description1')
        self.assertEqual(testInput.username, 'username1')
        self.assertEqual(testInput.email, 'email1@gmail.com')


