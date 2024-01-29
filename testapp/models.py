from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profiles(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  token = models.UUIDField(default=uuid.uuid4, editable=False)
  is_verified = models.BooleanField(default=False)
