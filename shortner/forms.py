from django import forms
from .models import ShortUrl


class ShortURLForm(forms.ModelForm):
    class Meta:
        model = ShortUrl
        fields = ['original_url' , 'expires_at']
        widgets = {
            'expires_at' : forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
        