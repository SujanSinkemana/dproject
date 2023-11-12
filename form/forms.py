from django import forms
from django.forms import ModelForm
from myapp.models import Student,StudentProfile

class StudentForm(forms.Form):
    name= forms.CharField(max_length=50)
    age = forms.IntegerField()
    department= forms.CharField(max_length=50)


class StudentModelForm(ModelForm):
    # adds new fields or override fields
    class Meta:
        model  = Student
        fields = ["name", "age", "department"]
