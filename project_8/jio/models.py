from django.db import models

# Create your models here.



# models.py
class Website(models.Model):
	name = models.CharField(max_length=50)
	website_Main_Img = models.ImageField(upload_to='images/')
