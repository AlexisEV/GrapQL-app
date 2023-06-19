import graphene

# Definiendo los datos
class User(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()

users_data = [
    User(id="1", name="John Doe", email="john.doe@example.com"),
    User(id="2", name="Jane Doe", email="jane.doe@example.com")
]

class Query(graphene.ObjectType):
    users = graphene.List(User)
    user = graphene.Field(User, id=graphene.ID(required=True))

    def resolve_users(self, info):
        return users_data

    def resolve_user(self, info, id):
        for user in users_data:
            if user.id == id:
                return user
        return None

# Creando el esquema
schema = graphene.Schema(query=Query)

'''
result = schema.execute("""
{
  user(id: "1") {
    id
    name
    email
  }
}
""")
'''

result = schema.execute("""
{
  users {
    id
    name
    email
  }
}
""")

print(result.data)