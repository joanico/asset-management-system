from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Employee, Asset
from .forms import EmployeeForm, AssetForm

# Employee Views
class EmployeeListView(ListView):
    model = Employee
    template_name = 'asset_app/employee_list.html'
    context_object_name = 'employees'

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'asset_app/employee_form.html'
    success_url = reverse_lazy('asset_app:employee_list')

    def form_valid(self, form):
        messages.success(self.request, 'Employee created successfully!')
        return super().form_valid(form)

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'asset_app/employee_form.html'
    success_url = reverse_lazy('asset_app:employee_list')

    def form_valid(self, form):
        messages.success(self.request, 'Employee updated successfully!')
        return super().form_valid(form)

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'asset_app/employee_confirm_delete.html'
    success_url = reverse_lazy('asset_app:employee_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Employee deleted successfully!')
        return super().delete(request, *args, **kwargs)

# Asset Views
class AssetListView(ListView):
    model = Asset
    template_name = 'asset_app/asset_list.html'
    context_object_name = 'assets'

class AssetCreateView(CreateView):
    model = Asset
    form_class = AssetForm
    template_name = 'asset_app/asset_form.html'
    success_url = reverse_lazy('asset_app:asset_list')

    def form_valid(self, form):
        messages.success(self.request, 'Asset created successfully!')
        return super().form_valid(form)

class AssetUpdateView(UpdateView):
    model = Asset
    form_class = AssetForm
    template_name = 'asset_app/asset_form.html'
    success_url = reverse_lazy('asset_app:asset_list')

    def form_valid(self, form):
        messages.success(self.request, 'Asset updated successfully!')
        return super().form_valid(form)

class AssetDeleteView(DeleteView):
    model = Asset
    template_name = 'asset_app/asset_confirm_delete.html'
    success_url = reverse_lazy('asset_app:asset_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Asset deleted successfully!')
        return super().delete(request, *args, **kwargs)
