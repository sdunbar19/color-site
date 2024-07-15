from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

def validate_hsv(value):
    if value < 0 or value > 255:
        raise ValidationError("Please enter a number between 0 and 255, inclusive.")
    return value

class Image(models.Model):
    image = models.ImageField(upload_to='post_images')
    
    def __str__(self):
        return self.image.name
    
class HSV(models.Model):
    hue = models.IntegerField(validators = [validate_hsv])
    saturation = models.IntegerField(validators = [validate_hsv])
    value = models.IntegerField(validators = [validate_hsv])

    def __str__(self):
        return str(self.hue) + ":" + str(self.saturation) + ":" + str(self.value)
