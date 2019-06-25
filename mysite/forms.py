from django import forms
from crispy_forms.helper import FormHelper


class ContactForm(forms.Form):
    helper = FormHelper()
    helper.form_show_labels = False
    name = forms.CharField(required=False, max_length=100, help_text="Name")
    email = forms.EmailField(required=True, help_text="Email")
    phone = forms.CharField(required=False, max_length=10, help_text="Phone")
    text = forms.CharField(required=True, widget=forms.Textarea, help_text="Message")

