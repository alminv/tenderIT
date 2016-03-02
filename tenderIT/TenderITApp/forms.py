from django import forms
from django.contrib.auth.models import User
from .models import (Company, Project)


# form used to register a new user
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = User
		fields = ('username','password')

class CompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ('name', 'nationalID', 'street','city','country','postcode', 'email', 'phone', 'website')	
	
#class Registration_form(UserCreationForm):
 #   class Meta:
  #      model = Company
  #      fields = ('name', 'username', 'email', 'password1', 'password2')

 #   def save(self, commit=True):
 #       user = super(Registration_form, self).save(commit = False)
 #       user.email = self.cleaned_data['email']
 #       if commit:
 #           user.save()
 #       return user

# form to add new project
class Post_project(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'budget', 'currency', 'startDate', 'endDate', 'documents', 'slug')

