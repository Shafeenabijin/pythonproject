from django.db import models

# Create your models here.

class place(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()
    img=models.ImageField(upload_to='picture')
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

