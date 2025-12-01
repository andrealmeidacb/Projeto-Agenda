from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image*/',
            }
        )
    )

    class Meta:
        model = models.Contact
        fields = (
            'fisrt_name', 'last_name', 'phone',
            'email', 'description', 'category',
            'picture',
        )


    def clean(self):
        cleaned_data = self.cleaned_data
        fisrt_name = self.cleaned_data.get('fisrt_name')
        last_name = self.cleaned_data.get('last_name')

        if fisrt_name == last_name:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )
            self.add_error('fisrt_name', msg)
            self.add_error('last_name', msg)

        return super().clean()
    

    def clean_first_name(self):
        fisrt_name = self.cleaned_data.get('fisrt_name')

        msg = ValidationError(
                'Veio do add_error',
                code='invalid'
            )

        if fisrt_name == 'ABC':
            self.add_error('first_name', msg)
