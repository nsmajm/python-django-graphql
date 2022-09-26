import graphene
from .user_types import UserType
from .user_input import UserInput
from .models import User
from django.contrib.auth.hashers import make_password


class CreateUserMutation(graphene.Mutation):
    class Arguments:
        user_data = UserInput()

    user = graphene.Field(UserType)

    def mutate(self, info, user_data=None):
        print(user_data)
        user_instance = User(
            name=user_data.name,
            email=user_data.email,
            password=make_password(user_data.password),
            phone_number=user_data.phone_number
        )
        user_instance.save()
        return CreateUserMutation(user=user_instance)


class UpdateUserMutation(graphene.Mutation):
    class Arguments:
        user_data = UserInput()

    user = graphene.Field(UserType)

    def mutate(self, info, user_data=None):
        user_instance = User.objects.get(id=user_data.id)
        user_instance.name = user_data.name
        user_instance.email = user_data.email
        user_instance.password = make_password(user_data.password)
        user_instance.phone_number = user_data.phone_number

        user_instance.save()

        return UpdateUserMutation(user=user_instance);
