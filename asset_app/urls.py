from django.urls import path
from . import views

app_name = 'asset_app'

urlpatterns = [
    # Employee URLs
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
    path('employee/add/', views.EmployeeCreateView.as_view(), name='employee_add'),
    path('employee/<int:pk>/edit/', views.EmployeeUpdateView.as_view(), name='employee_edit'),
    path('employee/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),

    # Asset URLs
    path('assets/', views.AssetListView.as_view(), name='asset_list'),
    path('asset/add/', views.AssetCreateView.as_view(), name='asset_add'),
    path('asset/<int:pk>/edit/', views.AssetUpdateView.as_view(), name='asset_edit'),
    path('asset/<int:pk>/delete/', views.AssetDeleteView.as_view(), name='asset_delete'),
] 