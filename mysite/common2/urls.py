from django.urls import path

from common2 import views

app_name = "common2"

urlpatterns = [
    path('register/', views.common2_register, name='register'),
]