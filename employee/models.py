from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ChangePassword(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     forgot_password_token = models.CharField(max_length=100)
     created_at = models.DateTimeField(auto_now_add=True)
    
    