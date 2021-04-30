"""
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage, name="homepage"),
    path('form-send_database/', views.Send_database, name="formDatabase"),
    path('deletedata/', views.DeleteData, name="delete"),
    path('editData/', views.Edit_data, name="edit_data"),

]
