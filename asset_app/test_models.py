from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Employee, Asset

class EmployeeModelTest(TestCase):
    def setUp(self):
        self.employee_data = {
            'full_name': 'John Doe',
            'work_email': 'john.doe@company.com',
            'country': 'AUS'
        }

    def test_create_employee(self):
        employee = Employee.objects.create(**self.employee_data)
        self.assertEqual(employee.full_name, self.employee_data['full_name'])
        self.assertEqual(employee.work_email, self.employee_data['work_email'])
        self.assertEqual(employee.country, self.employee_data['country'])

    def test_employee_str(self):
        employee = Employee.objects.create(**self.employee_data)
        self.assertEqual(str(employee), employee.full_name)

    def test_employee_email_unique(self):
        Employee.objects.create(**self.employee_data)
        with self.assertRaises(Exception):
            Employee.objects.create(**self.employee_data)

    def test_other_country_required(self):
        employee_data = self.employee_data.copy()
        employee_data['country'] = 'OTH'
        employee_data['other_country'] = ''  # Empty other_country
        
        with self.assertRaises(ValidationError) as context:
            employee = Employee(**employee_data)
            employee.full_clean()
        
        self.assertIn('other_country', context.exception.error_dict)

    def test_other_country_not_required_for_normal_country(self):
        employee_data = self.employee_data.copy()
        employee_data['country'] = 'AUS'
        employee_data['other_country'] = ''  # Empty other_country is fine for normal country
        
        try:
            employee = Employee(**employee_data)
            employee.full_clean()
            employee.save()
        except ValidationError:
            self.fail("ValidationError raised unexpectedly!")

class AssetModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            full_name='John Doe',
            work_email='john.doe@company.com',
            country='AUS'
        )
        self.asset_data = {
            'asset_type': 'LAPTOP',
            'asset_name': 'MacBook Pro 2023',
            'serial_number': 'MBP2023001',
            'responsible_person': self.employee,
            'location': 'Main Office',
            'is_working': True
        }

    def test_create_asset(self):
        asset = Asset.objects.create(**self.asset_data)
        self.assertEqual(asset.asset_type, self.asset_data['asset_type'])
        self.assertEqual(asset.asset_name, self.asset_data['asset_name'])
        self.assertEqual(asset.serial_number, self.asset_data['serial_number'])
        self.assertEqual(asset.responsible_person, self.employee)

    def test_asset_str(self):
        asset = Asset.objects.create(**self.asset_data)
        expected_str = f"{asset.get_asset_type_display()} - {asset.asset_name} ({asset.serial_number})"
        self.assertEqual(str(asset), expected_str) 