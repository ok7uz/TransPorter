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
            'loading_date': forms.DateInput(attrs={'type': 'date'}, format='YYYY-MM-DD'),
            'unloading_date': forms.DateInput(attrs={'type': 'date'}, format='YYYY-MM-DD'),
            'business_trip': forms.Textarea(attrs={'rows': 3}),
            'additional': forms.Textarea(attrs={'rows': 3}),
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
