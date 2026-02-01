from django.urls import path
from .views import DashboardView , RedirectURLView , URLDeleteView , URLEditview

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
 
    path('edit/<int:pk>/', URLEditview.as_view(), name='edit_url'),
    path('delete/<int:pk>/', URLDeleteView.as_view(), name='delete_url'),
    path('<str:code>/', RedirectURLView.as_view(), name='redirect'),
]
