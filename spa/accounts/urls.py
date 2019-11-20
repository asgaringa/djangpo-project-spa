from django.urls import path
from accounts import views


app_name = 'accounts'

urlpatterns = [
    path('login_success', views.login_success, name='login_sucess'),
]