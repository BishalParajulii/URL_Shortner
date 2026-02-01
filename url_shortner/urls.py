
from django.contrib import admin
from django.urls import path, include
from shortner.urls import RedirectURLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('shortner/',include('shortner.urls')),
    
    path("<str:code>/", RedirectURLView.as_view(), name="redirect"),
]
