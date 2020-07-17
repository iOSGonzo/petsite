from django import forms
from pet.models import Pet, Appointment


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['pet_name', 'species','breed', "weight_in_pounds", "owner"]

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date_of_appointment', 'duration_minutes','special_instructions', "pet"]
