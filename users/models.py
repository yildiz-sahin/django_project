from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from blog.models import Post


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name="Deneme --> test", on_delete=models.CASCADE)
    image = models.ImageField('Image you want always', default='default.jpg', upload_to='profile_pics', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            resize = (300, 300)
            img.thumbnail(resize)
            img.save(self.image.path)
