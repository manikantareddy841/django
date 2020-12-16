from django import forms

class feedbackform(forms.Form):
    name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'enter your name'
            }
        )
    )
    rating=forms.IntegerField(
        label='Enter your rating',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'enter your rating'
            }
        )
    )
    feedback=forms.CharField(
        label='Enter your feedback',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeolder':'your feedback'
            }
        )
    )