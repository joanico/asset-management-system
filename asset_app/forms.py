from django import forms
from .models import Asset, Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name', 'work_email', 'country', 'other_country']

    def clean(self):
        cleaned_data = super().clean()
        country = cleaned_data.get('country')
        other_country = cleaned_data.get('other_country')
        
        if country == 'OTH' and not other_country:
            raise forms.ValidationError("Please specify the other country.")
        return cleaned_data

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = [
            'asset_type', 'other_asset_type', 'asset_name', 'serial_number',
            'responsible_person', 'location', 'is_working', 'has_adapters',
            'adapter_details', 'charger_replaced', 'number_of_chargers',
            'charger_locations'
        ]

    def clean(self):
        cleaned_data = super().clean()
        asset_type = cleaned_data.get('asset_type')
        other_asset_type = cleaned_data.get('other_asset_type')
        
        if asset_type == 'OTHER' and not other_asset_type:
            raise forms.ValidationError("Please specify the other asset type.")
        return cleaned_data 