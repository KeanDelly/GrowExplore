from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	staffVerification = forms.CharField(required=False)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2", "staffVerification")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user






