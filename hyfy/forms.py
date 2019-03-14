from django import forms
from django.contrib.auth.models import User
from hyfy.models import UserProfile, Review
from django.utils import datetime_safe

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	picture = forms.ImageField(required=False)

	class Meta:
		model = UserProfile
		exclude = ('user',)

class ReviewForm(forms.ModelForm):
	text = forms.CharField(max_length=200, help_text="Please enter a review")
	# review = forms.IntegerField(widget=forms.HiddenInput())
	# date = forms.DateField(widget=forms.HiddenInput())

	class Meta:
		model = Review
		fields = ('text',)