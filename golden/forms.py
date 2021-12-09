from golden.models import Profile, Project, Reviews
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# The signup form
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=300, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'profile_picture', 'profile_bio']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','profile']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        exclude = ['user','project','average']