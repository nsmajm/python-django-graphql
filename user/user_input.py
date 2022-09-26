import graphene


class UserInput(graphene.InputObjectType):
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()
    password = graphene.String()
    phone_number = graphene.String()

