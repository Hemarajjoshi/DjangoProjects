from django.db import models

# Create your models here.

class Viewers(models.Model):
    username = models.CharField(max_length = 100, primary_key = True)
    password = models.CharField(max_length = 100)


    class Meta:
          verbose_name_plural = "Viewers"


class Paticipant(models.Model):
    username = models.CharField(max_length = 100)
    email = models.EmailField(primary_key = True)
    password = models.CharField(max_length = 100)
    project_name = models.CharField(max_length= 100)
    project_description = models.CharField(max_length = 500)
    project_photo = models.ImageField()
    prepared_by = models.CharField(max_length = 100)



