from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)
    role_id= models.IntegerField(blank=True, null=True,default=1)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)  # default
    updated_at = models.DateTimeField(auto_now=True, blank=True)  # default  value

    def __str__(self):
        return self.name

    class Meta:
        db_table = "users"
