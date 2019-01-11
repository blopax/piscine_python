from django import forms


class FormHistory(forms.Form):
    text_field = forms.CharField(required=True)
