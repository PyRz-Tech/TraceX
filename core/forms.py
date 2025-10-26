from django import forms

class StockForm(forms.Form):
    symbol = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter ticker (e.g., IBM)'
    }))
    interval = forms.ChoiceField(choices=[
        ('5min', '5 Minutes'),
        ('15min', '15 Minutes'),
        ('30min', '30 Minutes'),
        ('60min', '60 Minutes'),
    ], widget=forms.Select(attrs={
        'class': 'form-select'
    }))
