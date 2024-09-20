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
            'paid_to',
            'remaining_amount',
            'business_trip',
            'additional',
            'status'
        ]
        widgets = {
            'route': forms.TextInput(attrs={'class': 'border-dark'}),
            'transport_price': forms.TextInput(attrs={'class': 'border-dark'}),
            'advance_payment': forms.TextInput(attrs={'class': 'border-dark'}),
            'license_plate': forms.TextInput(attrs={'class': 'border-dark'}),
            'cargo_owner': forms.TextInput(attrs={'class': 'border-dark'}),
            'loading_date': forms.DateInput(attrs={'type': 'date', 'class': 'border-dark'}, format='YYYY-MM-DD'),
            'unloading_date': forms.DateInput(attrs={'type': 'date', 'class': 'border-dark'}, format='YYYY-MM-DD'),
            'paid_to': forms.TextInput(attrs={'class': 'border-dark'}),
            'remaining_amount': forms.TextInput(attrs={'class': 'border-dark'}),
            'business_trip': forms.Textarea(attrs={'rows': 3, 'class': 'border-dark'}),
            'additional': forms.Textarea(attrs={'rows': 3, 'class': 'border-dark'}),
            'status': forms.Select(attrs={'class': 'border-dark'})

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


class TransportationUpdateForm(forms.ModelForm):
    status = forms.Field(
        widget=forms.Select(attrs={'class': 'border-dark-subtle', 'readonly': 'readonly'}, choices=Transportation.StatusColors.choices),
        required=False,
        label='Статус',
    )

    def __init__(self, is_admin=False, *args, **kwargs):
        self.is_admin = is_admin

        super().__init__(*args, **kwargs)


    class Meta:
        model = Transportation
        attrs = {'class': 'border-dark-subtle', 'readonly': 'readonly'}
        fields = [
            'route',
            'transport_price',
            'advance_payment',
            'license_plate',
            'cargo_owner',
            'loading_date',
            'unloading_date',
            'paid_to',
            'remaining_amount',
            'business_trip',
            'additional',
            'status'
        ]
        widgets = {
            'route': forms.TextInput(attrs=attrs),
            'transport_price': forms.TextInput(attrs=attrs),
            'advance_payment': forms.TextInput(attrs=attrs),
            'license_plate': forms.TextInput(attrs=attrs),
            'cargo_owner': forms.TextInput(attrs=attrs),
            'loading_date': forms.DateInput(attrs={'type': 'date', **attrs}, format='%Y-%m-%d'),
            'unloading_date': forms.DateInput(attrs={'type': 'date', **attrs}, format='%Y-%m-%d'),
            'paid_to': forms.TextInput(attrs=attrs),
            'remaining_amount': forms.TextInput(attrs={'class': 'border-dark'}),
            'business_trip': forms.TextInput(attrs={'class': 'border-dark'}),
            'additional': forms.Textarea(attrs={'rows': 3, **attrs}),

        }

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        remaining_amount = cleaned_data['remaining_amount']
        business_trip = cleaned_data['business_trip']

        transportation = super().save(commit=False)
        transportation.remaining_amount = remaining_amount
        transportation.business_trip = business_trip
        if commit:
            transportation.save()
        return transportation


class TransportationAdminUpdateForm(TransportationUpdateForm):
    status = forms.Field(
        widget=forms.Select(attrs={'class': 'border-dark',}, choices=Transportation.StatusColors.choices),
        required=False,
        label='Статус',
    )

    class Meta:
        model = Transportation
        attrs = {'class': 'border-dark'}
        fields = [
            'route',
            'transport_price',
            'advance_payment',
            'license_plate',
            'cargo_owner',
            'loading_date',
            'unloading_date',
            'paid_to',
            'remaining_amount',
            'business_trip',
            'additional',
            'status'
        ]
        widgets = {
            'route': forms.TextInput(attrs=attrs),
            'transport_price': forms.TextInput(attrs=attrs),
            'advance_payment': forms.TextInput(attrs=attrs),
            'license_plate': forms.TextInput(attrs=attrs),
            'cargo_owner': forms.TextInput(attrs=attrs),
            'loading_date': forms.DateInput(attrs={'type': 'date', **attrs}, format='%Y-%m-%d'),
            'unloading_date': forms.DateInput(attrs={'type': 'date', **attrs}, format='%Y-%m-%d'),
            'paid_to': forms.TextInput(attrs=attrs),
            'remaining_amount': forms.TextInput(attrs={'class': 'border-dark'}),
            'business_trip': forms.TextInput(attrs={'class': 'border-dark'}),
            'additional': forms.Textarea(attrs={'rows': 3, **attrs}),

        }