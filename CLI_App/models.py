from django.db import models

# Create your models here.
class Command(models.Model):
    input_text = models.CharField(max_length=255)
    output_text = models.TextField()
