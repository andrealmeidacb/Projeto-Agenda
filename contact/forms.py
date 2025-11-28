from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    fisrt_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init',
            }
        ),
        help_text='Texto de ajuda para seu usuario'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, ** kwargs)

        # self.fields['fisrt_name'].widget.attrs.update({
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Aqui veio do init',
        # })

    class Meta:
        model = models.Contact
        fields = (
            'fisrt_name', 'last_name', 'phone',
            'email', 'description', 'category',
        )
        # widgets = {
        #     'fisrt_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui'
        #         }
        #     )
        # }

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
    
    # def clean_first_name(self):
    #     fisrt_name = self.cleaned_data.get("fisrt_name")
    
    #     if fisrt_name == 'ABC':
    #         self.add_error(
    #             'fisrt_name',
    #             ValidationError(
    #                 'Veio do add_error',
    #                 code='invalid'
    #             )
    #         )

    #     return fisrt_name
