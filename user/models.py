from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # default
    updated_at = models.DateTimeField(auto_now=True, null=True)  # default  value

    def __str__(self):
        return self.name

    class Meta:
        db_table = "users"
