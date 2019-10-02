from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from .models import Client
from schwifty import IBAN

class CreatedFormsClient(BSModalForm):
    class Meta:
        model = Client
        #fields ='__all__'
        exclude = ['userCreated']

    def clean_iban(self):
        try:
            iban = IBAN(self.cleaned_data['iban'])
            return iban.formatted
        except Exception as e:
            raise forms.ValidationError(e)