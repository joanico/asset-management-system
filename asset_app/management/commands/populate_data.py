from django.core.management.base import BaseCommand
from django.db import transaction
from asset_app.models import Employee, Asset
import random

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting to populate database...')

        try:
            with transaction.atomic():
                # Create sample employees
                employees = [
                    Employee.objects.create(
                        full_name='John Doe',
                        work_email='john.doe@company.com',
                        country='AUS'
                    ),
                    Employee.objects.create(
                        full_name='Jane Smith',
                        work_email='jane.smith@company.com',
                        country='TL'
                    ),
                    Employee.objects.create(
                        full_name='Bob Johnson',
                        work_email='bob.johnson@company.com',
                        country='PNG'
                    ),
                ]

                # Sample asset data
                assets_data = [
                    {
                        'asset_type': 'LAPTOP',
                        'asset_name': 'MacBook Pro 2023',
                        'serial_number': 'MBP2023001',
                        'location': 'Main Office',
                        'is_working': True,
                        'has_adapters': True,
                        'adapter_details': 'HDMI, USB-C Hub',
                        'charger_replaced': False,
                        'number_of_chargers': 2,
                        'charger_locations': 'Home and Office'
                    },
                    {
                        'asset_type': 'MONITOR',
                        'asset_name': 'Dell U2419H',
                        'serial_number': 'DELL001',
                        'location': 'Branch Office',
                        'is_working': True,
                        'has_adapters': True,
                        'adapter_details': 'DisplayPort cable',
                        'number_of_chargers': 1,
                        'charger_locations': 'Office'
                    },
                    {
                        'asset_type': 'MOBILE',
                        'asset_name': 'iPhone 14',
                        'serial_number': 'IPH14001',
                        'location': 'Mobile',
                        'is_working': True,
                        'has_adapters': True,
                        'adapter_details': 'Lightning cable, wireless charger',
                        'charger_replaced': True,
                        'number_of_chargers': 2,
                        'charger_locations': 'Home and Office'
                    }
                ]

                # Create assets and assign to random employees
                for asset_data in assets_data:
                    Asset.objects.create(
                        responsible_person=random.choice(employees),
                        **asset_data
                    )

            self.stdout.write(self.style.SUCCESS('Successfully populated the database!'))
            self.stdout.write(f'Created {len(employees)} employees and {len(assets_data)} assets.')

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error populating database: {str(e)}')) 