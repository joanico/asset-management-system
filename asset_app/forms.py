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
            'responsible_person', 'location', 'is_working', 'status',
            'condition_details', 'has_adapters', 'adapter_details',
            'charger_replaced', 'number_of_chargers', 'charger_locations'
        ]
        widgets = {
            'condition_details': forms.Textarea(attrs={'rows': 3}),
            'adapter_details': forms.Textarea(attrs={'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        asset_type = cleaned_data.get('asset_type')
        other_asset_type = cleaned_data.get('other_asset_type')
        status = cleaned_data.get('status')
        condition_details = cleaned_data.get('condition_details')
        
        if asset_type == 'OTHER' and not other_asset_type:
            raise forms.ValidationError("Please specify the other asset type.")
        
        if status == 'POOR' and not condition_details:
            raise forms.ValidationError("Please provide details about the asset's condition when status is 'Not in Good Condition'.")
        
        return cleaned_data 