from django.db import models
from django.core.exceptions import ValidationError

# Country choices
COUNTRY_CHOICES = [
    ('TL', 'Timor Leste'),
    ('PNG', 'Papua New Guinea'),
    ('AUS', 'Australia'),
    ('FJI', 'Fiji'),
    ('IDN', 'Indonesia'),
    ('OTH', 'Other'),
]

# Asset type choices
ASSET_TYPE_CHOICES = [
    ('LAPTOP', 'Laptop'),
    ('MONITOR', 'Monitor'),
    ('MOBILE', 'Mobile Phone'),
    ('OTHER', 'Other'),
]

# Asset status choices
ASSET_STATUS_CHOICES = [
    ('GOOD', 'Good Condition'),
    ('MAINTENANCE', 'Under Maintenance'),
    ('POOR', 'Not in Good Condition'),
]

class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    work_email = models.EmailField(unique=True)
    country = models.CharField(
        max_length=3,
        choices=COUNTRY_CHOICES,
        help_text="Select the country where employee is based"
    )
    other_country = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Specify country if 'Other' is selected"
    )

    def clean(self):
        super().clean()
        if self.country == 'OTH' and not self.other_country:
            raise ValidationError({
                'other_country': 'Other country must be specified when country is set to Other'
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name

class Asset(models.Model):
    # Asset Information
    asset_type = models.CharField(
        max_length=10,
        choices=ASSET_TYPE_CHOICES
    )
    other_asset_type = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Specify asset type if 'Other' is selected"
    )
    asset_name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    responsible_person = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT,
        related_name='responsible_assets'
    )
    location = models.CharField(max_length=200)
    is_working = models.BooleanField(
        default=True,
        help_text="Is the device in good working condition?"
    )
    status = models.CharField(
        max_length=20,
        choices=ASSET_STATUS_CHOICES,
        default='GOOD',
        help_text="Current status of the asset"
    )
    condition_details = models.TextField(
        blank=True,
        null=True,
        help_text="Additional details about the asset's condition (required if status is 'Not in Good Condition')"
    )

    # Additional Information
    has_adapters = models.BooleanField(
        default=False,
        help_text="Do you have any adapters (HDMI, USB-C, etc)?"
    )
    adapter_details = models.TextField(
        blank=True,
        null=True,
        help_text="Specify which adapters you have"
    )
    charger_replaced = models.BooleanField(
        default=False,
        help_text="Have you ever had your laptop charger replaced?"
    )
    number_of_chargers = models.PositiveSmallIntegerField(
        default=1,
        help_text="How many chargers do you keep?"
    )
    charger_locations = models.CharField(
        max_length=200,
        blank=True,
        help_text="Where do you keep your chargers? (e.g., home/office)"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()
        if self.status == 'POOR' and not self.condition_details:
            raise ValidationError({
                'condition_details': 'Condition details are required when status is "Not in Good Condition"'
            })
        if self.asset_type == 'OTHER' and not self.other_asset_type:
            raise ValidationError({
                'other_asset_type': 'Other asset type must be specified when asset type is set to Other'
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_asset_type_display()} - {self.asset_name} ({self.serial_number})"
