import graphene
from graphene_django import DjangoObjectType
from .user_types import UserType
from .mutation import CreateUserMutation,UpdateUserMutation


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    find_user = graphene.Field(UserType, name=graphene.String())

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_find_user(root, info, name):
        return User.objects.get(name__contains=name)


class Mutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()
    update_user = UpdateUserMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
