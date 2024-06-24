import strawberry

@strawberry.input
class StatusASrgs:
    status: bool  = strawberry.UNSET