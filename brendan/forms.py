from django import forms
from crispy_forms.helper import FormHelper

#TODO: makeover the contact form
class ContactForm(forms.Form):
    """Email contact form"""
    helper = FormHelper()
    name = forms.CharField(required=True,  widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email'}))
    message = forms.CharField(required=True, widget=forms.Textarea())
