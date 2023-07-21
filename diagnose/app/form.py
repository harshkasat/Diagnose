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
    medical_condition = forms.ChoiceField(
        # choices=MEDICAL_CONDITION_CHOICES,
        # widget=forms.Select(attrs={'class': 'form-control'})
        widget=forms.Select(choices=MEDICAL_CONDITION_CHOICES)
    )


    # favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=FRUIT_CHOICES))