# forms.py

from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

MEDICAL_CONDITION_CHOICES = [
    ('brain_tumor', 'Brain Tumor'),
    ('chest_xray', 'Chest X-ray'),
    ('melanoma', 'Melanoma'),
]

class MedicalConditionForm(forms.Form):
    medical_condition = forms.ChoiceField(choices=MEDICAL_CONDITION_CHOICES, label='Medical Condition',widget=forms.Select(attrs={'id': 'option'}))
