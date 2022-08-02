from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
# Create your models here.

class User(AbstractUser):
    is_company=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=False)


    def __str__(self):
        return self.username    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



class Company(models.Model):
    user=models.OneToOneField(User, related_name="company", on_delete=models.CASCADE)
    comp_phone=models.CharField(default="", max_length=10, null=True, blank=True)
    comp_email=models.EmailField(max_length=100, null=True, blank=True)
    comp_address=models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Customer(models.Model):
    user=models.OneToOneField(User, related_name="customer", on_delete=models.CASCADE)
    phone=models.CharField(default="", max_length=10, null=True, blank=True)
    email=models.EmailField(max_length=100, null=True, blank=True)
    address=models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.user.username
