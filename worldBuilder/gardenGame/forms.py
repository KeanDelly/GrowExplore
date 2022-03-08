from dataclasses import field
import datetime
from django import forms
from django.forms import ModelForm
from .models import buildingOfTheDay
from django.db.models.fields import BLANK_CHOICE_DASH


# Create your forms here.

# From used in the BOTD page to input the building of the day information
class buildingForm(ModelForm):
    class Meta:
        model = buildingOfTheDay
        fields = ('building_name', 'building_desc', 'date', 'reward')

    CHOICES = [('Harrison Building', 'Harrison Building'),
               ('Amory Building', 'Amory Building'),
               ('The Forum', 'The Forum'),
               ('Business School Building One', 'Business School Building One'),
               ('Cornwall House Swimming Pool', 'Cornwall House Swimming Pool'),
               ('Northcott Theatre', 'Northcott Theatre'),
               ('Geoffrey Pope', 'Geoffrey Pope'),
               ('Great Hall', 'Great Hall'),
               ('Hatherly', 'Hatherly'),
               ('Henry Wellcome Building for Biocatalysis', 'Henry Wellcome Building for Biocatalysis'),
               ('Innovation One | South West Institute of Technology', 'Innovation One | South West Institute of Technology'),
               ('Institute of Arab and Islamic Studies', 'Institute of Arab and Islamic Studies'),
               ('INTO International Study Centre', 'INTO International Study Centre'),
               ('Laver', 'Laver'),
               ('Living Systems', 'Living Systems'),
               ('Mary Harris Memorial Chapel', 'Mary Harris Memorial Chapel'),
               ('Old Library', 'Old Library'),
               ('Peter Chalk Centre', 'Peter Chalk Centre'),
               ('Physics', 'Physics'),
               ('Queens', 'Queens'),
               ('Reed Hall', 'Reed Hall'),
               ('Reed Mews Wellbeing Centre', 'Reed Mews Wellbeing Centre'),
               ('Sir Henry Wellcome Building for Mood Disorders Research', 'Sir Henry Wellcome Building for Mood Disorders Research'),
               ('Sports Park', 'Sports Park'),
               ('Streatham Court', 'Streatham Court'),
               ('Student Health Centre', 'Student Health Centre'),
               ('Washington Singer', 'Washington Singer'),
               ('Xfi', 'Xfi')]
    building_name = forms.CharField(label="Building Name", widget=forms.Select(choices=BLANK_CHOICE_DASH+CHOICES, attrs={'placeholder': 'Select building'}))
    building_desc = forms.CharField(label="Description", max_length=200, widget=forms.widgets.TextInput())
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), initial=datetime.date.today)
    reward = forms.CharField(label="Daily Reward", max_length=200)
