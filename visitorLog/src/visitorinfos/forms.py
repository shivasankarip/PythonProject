from django import forms

from .models import VisitorInfo


#form to get the user input values
class VisitorInfoForm(forms.ModelForm):
    class Meta:
        model=VisitorInfo

        

