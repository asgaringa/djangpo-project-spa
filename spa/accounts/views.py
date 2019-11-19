from django.shortcuts import render, redirect

# Create your views here.

def login_success(request):
  if request.user.is_superuser:
    return redirect('admin')
  else:
    return redirect('home')
