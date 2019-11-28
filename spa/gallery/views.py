from django.shortcuts import render
from django.views.generic import ListView
from .models import Gallery
# Create your views here.

class GalleryView(ListView):
  model = Gallery
  template_name='gallery/gallery.html'