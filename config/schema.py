import strawberry
from rooms import schema as room_schema


@strawberry.type
class Query(room_schema.Query):
    pass


@strawberry.type
class Mutation(room_schema.Mutation):
    pass


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
)
