from django import forms
from .models import Website
 
 
class WebsiteForm(forms.ModelForm):
 
    class Meta:
        model = Website
        fields = ['name', 'website_Main_Img']