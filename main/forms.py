
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .mongo import mongodata

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
class NameForm(forms.Form):
    db = mongodata()
    trainerList = db.trainer_names()
    Trainer = forms.ChoiceField(choices=[(x, x) for x in trainerList])
    collegeList = db.college_names()
    College = forms.ChoiceField(choices=[(x, x) for x in collegeList])
    Start_Date = forms.DateField()
    Start_Date.widget.attrs.update({'class': 'datepicker'})
    End_Date = forms.DateField()
    End_Date.widget.attrs.update({'class': 'datepicker'})
    Hours_per_day = forms.IntegerField()
    c1 = [('online', 'Online'), ('offline', 'Offline')]
    Mode_of_Training = forms.ChoiceField(choices=c1, widget=forms.RadioSelect)
    Pay_per_day = forms.IntegerField()
    c2 = [('Yes', 'Yes'), ('No', 'No')]
    Food = forms.ChoiceField(choices=c2, widget=forms.RadioSelect)
    Accomodation = forms.ChoiceField(choices=c2, widget=forms.RadioSelect)

    def clean_Hours_per_day(self):
        hours = self.cleaned_data['Hours_per_day']
        if hours < 0:
            raise forms.ValidationError("Hours per day should be greater than zero")
        return hours

    def clean_Pay_per_day(self):
        pay = self.cleaned_data['Pay_per_day']
        if pay < 0:
            raise forms.ValidationError("Pay per day should be greater than zero")
        return pay

class TrainerForm(forms.Form):

    name = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
    phno = forms.CharField(max_length=200)
    location = forms.CharField(max_length=200)

    bank = forms.CharField(max_length=200)
    acc_no = forms.CharField(max_length=200)
    ifsc = forms.CharField(max_length=200)
    pan = forms.CharField(max_length=200)

class CollegeForm(forms.Form):
    name = forms.CharField(max_length=200)
    location = forms.CharField(max_length=200)
