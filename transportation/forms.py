from django import forms

from transportation.models import Transportation


class TransportationForm(forms.ModelForm):

    class Meta:
        model = Transportation
        fields = [
            'route',
            'transport_price',
            'advance_payment',
            'license_plate',
            'cargo_owner',
            'loading_date',
            'unloading_date',
            'remaining_amount',
            'business_trip',
            'additional',
        ]
        widgets = {
            'route': forms.TextInput(attrs={'class': 'border-dark'}),
            'transport_price': forms.TextInput(attrs={'class': 'border-dark'}),
            'advance_payment': forms.TextInput(attrs={'class': 'border-dark'}),
            'license_plate': forms.TextInput(attrs={'class': 'border-dark'}),
            'cargo_owner': forms.TextInput(attrs={'class': 'border-dark'}),
            'loading_date': forms.DateInput(attrs={'type': 'date', 'class': 'border-dark'}, format='YYYY-MM-DD'),
            'unloading_date': forms.DateInput(attrs={'type': 'date', 'class': 'border-dark'}, format='YYYY-MM-DD'),
            'remaining_amount': forms.TextInput(attrs={'class': 'border-dark'}),
            'business_trip': forms.Textarea(attrs={'rows': 3, 'class': 'border-dark'}),
            'additional': forms.Textarea(attrs={'rows': 3, 'class': 'border-dark'}),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.operator = user

    def save(self, commit=True):
        transportation = super().save(commit=False)
        transportation.operator = self.operator
        if commit:
            transportation.save()
        return transportation
