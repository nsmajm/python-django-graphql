import graphene
from graphene_django import DjangoObjectType
from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "name", "email", "phone_number", "created_at", "updated_at")

    def __str__(self):
        return self


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    find_user = graphene.Field(UserType, name=graphene.String())

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_find_user(root, info, name):
        return User.objects.get(name__contains=name)


schema = graphene.Schema(query=Query)
