from django.db import models

# Create your models here.

class Gallery(models.Model):
  title = models.TextField()
  cover = models.ImageField(upload_to='gallery/', blank=True)
  context_object_name = 'gallery_list'

  def __str__(self):
        return self.title
