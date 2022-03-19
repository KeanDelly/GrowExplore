from dataclasses import field
import datetime
from django import forms
from django.forms import ModelForm
from gardenGame.models import buildingOfTheDay, reportToAdmin
from django.db.models.fields import BLANK_CHOICE_DASH

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
REWARDS = [('birdbox.png', 'Bird Box'),
               ('gardenfork.png','Garden Fork'),
               ('rake.png', 'Rake'),
               ('spade.png', 'Spade'),
               ('wateringcan.png' , 'Watering Can'),
               ('wellies.png', 'Wellies'),
               ('wheelbarrow.png', "Wheel Barrow")]

# Create your forms here.

# From used in the BOTD page to input the building of the day information
class buildingForm(ModelForm):
    class Meta:
        model = buildingOfTheDay
        fields = ('name', 'description', 'date', 'reward')


    
    name = forms.CharField(label="Building Name", widget=forms.Select(choices=BLANK_CHOICE_DASH+CHOICES))
    description = forms.CharField(label="Description", max_length=200, widget=forms.Textarea(attrs={'rows':3, 'cols':43}))
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), initial=datetime.date.today)
    reward = forms.CharField(label="Daily Reward",  widget=forms.Select(choices=BLANK_CHOICE_DASH+REWARDS))
    #reward = forms.ImageField(label="Daily Reward",  widget=forms.Select(choices=BLANK_CHOICE_DASH+REWARDS))


class reportToAdminForm(ModelForm):
    class Meta:
        model = reportToAdmin
        fields = ('problem_name', 'problem_description', 'username', 'email')

        problem_description = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'rows':3, 'cols':43}))
        username = forms.CharField(widget=forms.TextInput())
        email = forms.CharField(widget=forms.EmailInput())

