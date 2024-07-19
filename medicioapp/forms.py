from django import forms
from medicioapp.models import Appointment,ImageModel

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields =['name','email','phone','date','department','doctor','message']

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image','title','price']