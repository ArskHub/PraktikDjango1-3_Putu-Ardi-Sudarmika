from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

# Custom validator function
def check_for_a(value):
    if value[0].lower() != 'a':
        raise ValidationError("Name needs to start with A")
    
class FormName(forms.Form):
    # Add the custom validator to the 'name' field
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Input your email again:')
    text = forms.CharField(widget=forms.Textarea)
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']
        
        if email != vemail:
            raise ValidationError("Make sure emails match!")