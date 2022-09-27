from graphene_django import DjangoObjectType
from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "name", "email", "phone_number", "created_at", "updated_at")

    def __str__(self):
        return self.name
