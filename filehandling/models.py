from django.db import models
from django.contrib.auth.models import User

class ImageForm(models.Model):
    user_id=models.ForeignKey(User, null = True , on_delete=models.CASCADE)
    user_name=models.CharField(max_length=100)
    image_file=models.ImageField(upload_to='Images/user_images/')


# Create your models here.
