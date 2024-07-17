from django import forms
from medicioapp.models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields =['name','email','phone','date','department','doctor','message']