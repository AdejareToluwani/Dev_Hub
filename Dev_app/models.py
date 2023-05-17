from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import User
import uuid


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # id_user = models.UUIDField(
    #     default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    img = models.ImageField(upload_to="users_image", default="")
    bio = models.TextField(blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    location = models.CharField(max_length=150, blank=True, null=True)
    # age = models.IntegerField()

    def __str__(self):
        return (f"{self.user}")

    # def __str__(self):
    #     return (f"Hy {self.user}")
