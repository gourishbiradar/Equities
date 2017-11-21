from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Most_Volatile_Futures

derivative_choices=(
    ('Futures','Futures',),
    ('Options','Options',),
    )
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    first_name=forms.CharField(max_length=20,help_text='Required')
    last_name=forms.CharField(max_length=20,help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email', 'password1', 'password2')
        

##class UpdateForm(forms.ModelForm):
##    class Meta:
##        model=User
##        fields=[
class VolatileDeriavativesForm(forms.Form):
    #selectType=forms.MultipleChoiceField(required=True,widget=forms.Select,choices=derivative_choices)
    selectType=forms.CharField(max_length=10,help_text="(Futures/Options)")
    
class DeriavativesForm(forms.Form):
    selectType=forms.CharField(max_length=10,help_text="(Futures/Options)")
    selectDate=forms.DateField()
    selectSymbol=forms.CharField(max_length=10,help_text="Symbol")

class SectorForm(forms.Form):
    sectorName=forms.CharField(max_length=30)

class FutureInvForm(forms.Form):
    selectSymbol=forms.CharField(max_length=10,help_text="Symbol")
    selectDate=forms.DateField()
    quantity=forms.IntegerField(required=True)

class OptionInvForm(forms.Form):
    selectSymbol=forms.CharField(max_length=10,help_text="Symbol")
    selectDate=forms.DateField()
    quantity=forms.IntegerField(required=True)
