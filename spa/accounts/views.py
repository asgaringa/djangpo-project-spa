from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def login_success(request):
  if request.user.is_superuser:
    return redirect('admin:index')
  else:
    return redirect('home')
