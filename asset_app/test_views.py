from django.test import TestCase, Client
from django.urls import reverse
from .models import Employee, Asset

class AssetViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.employee = Employee.objects.create(
            full_name='John Doe',
            work_email='john.doe@company.com',
            country='AUS'
        )
        self.asset = Asset.objects.create(
            asset_type='LAPTOP',
            asset_name='MacBook Pro 2023',
            serial_number='MBP2023001',
            responsible_person=self.employee,
            location='Main Office',
            is_working=True
        )

    def test_asset_list_view(self):
        response = self.client.get(reverse('asset_app:asset_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'asset_app/asset_list.html')
        self.assertIn('assets', response.context)

    def test_asset_create_view(self):
        response = self.client.get(reverse('asset_app:asset_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'asset_app/asset_form.html')

class EmployeeViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.employee = Employee.objects.create(
            full_name='John Doe',
            work_email='john.doe@company.com',
            country='AUS'
        )

    def test_employee_list_view(self):
        response = self.client.get(reverse('asset_app:employee_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'asset_app/employee_list.html')
        self.assertIn('employees', response.context)

    def test_employee_create_view(self):
        response = self.client.get(reverse('asset_app:employee_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'asset_app/employee_form.html') 