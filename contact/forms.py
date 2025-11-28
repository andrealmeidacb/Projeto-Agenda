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
            'fisrt_name', 'last_name', 'phone'
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
        # cleaned_data = self.cleaned_data

        self.add_error(
            'fisrt_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )

        self.add_error(
            'fisrt_name',
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )

        return super().clean()