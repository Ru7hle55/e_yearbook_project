from django import forms
from MYpetstagram.pets.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [
            'name',
            'date_of_birth',
            'personal_pet_photo',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Pet name',
            }),
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date',
            }),
            'personal_pet_photo': forms.TextInput(attrs={
                'placeholder': 'Link to Image',
            }),
        }
        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Date of Birth',
            'personal_pet_photo': 'Link to Image',
        }


class PetDeleteForm(PetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'


