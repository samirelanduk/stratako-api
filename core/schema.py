import graphene
from graphql import GraphQLError

class Query(graphene.ObjectType):
    """The root query object. It supplies the user attribute, which is the
    portal through which other attributes are accessed."""

    time = graphene.Int()
    user = graphene.Field("core.queries.UserType")

    def resolve_user(self, info, **kwargs):
        user = info.context.user
        if not user: raise GraphQLError('{"user": "Not authorized"}')
        return info.context.user


from core.mutations import SignupMutation, LoginMutation
from core.mutations import UpdateEmailMutation, UpdatePasswordMutation
from core.mutations import UpdateBasicSettingsMutation
from core.mutations import DeleteUserMutation
class Mutation(graphene.ObjectType):
    signup = SignupMutation.Field()
    login = LoginMutation.Field()
    update_email = UpdateEmailMutation.Field()
    update_password = UpdatePasswordMutation.Field()
    update_basic_settings = UpdateBasicSettingsMutation.Field()
    delete_user = DeleteUserMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)