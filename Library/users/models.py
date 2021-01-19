from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # departments = (("IT", "Information Technology"), ("C", "Civil Engineering"), ("MP", "Mechanical Engineering"), ("EcE", "Electronic Engineering"), ("EP", "Electrical Power"), ("McE", "Mechatronics Engineering"), ("Arch", "Architecture"))
    # department = models.CharField(max_length=20, choices=departments, default='Null Department')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output = (300, 300)
            img.thumbnail(output, Image.LANCZOS)
            img.save(self.image.path)
