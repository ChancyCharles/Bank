# forms.py
from django import forms
from .models import User, Application



class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'name', 'dob', 'age', 'gender', 'phone_number', 'mail_id', 'address',
          'account_type', 'materials'
        ]
        widgets = {
            'dob': forms.SelectDateWidget(years=range(1900, 2025)),
            'materials': forms.CheckboxSelectMultiple(choices=Application.MATERIAL_CHOICES),
        }