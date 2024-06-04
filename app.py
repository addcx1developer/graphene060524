import graphene
from mutation import CreateUser, UpdateUser, DeleteUser
from query import Query
from type import User
from graphene import Field, String, List

class MyMutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

class MyQuery(Query):
    user = Field(User)
    get_user = Field(User, id = String())
    get_users = List(User)

schema = graphene.Schema(query = MyQuery, mutation = MyMutations)

# result = schema.execute(
#     '''
#     mutation {
#         createUser(id: "2", name: "John Doe", email: "johndoe@example.com", password: "johndoe@2024"){
#             user {
#                 id,
#                 name,
#                 email,
#                 password
#             }
#         }
#     }
#     '''
# )

# print(result.data)