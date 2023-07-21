# models.py

from django.db import models
from django.contrib.auth import get_user_model

class UserProfileImage(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/')
    

    def __str__(self):
        return f"{self.user.username}'s Profile Image {self.id}"
