from django import forms
from pet.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['pet_name', 'species','breed', "weight_in_pounds", "owner"]
