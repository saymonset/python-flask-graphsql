import strawberry

@strawberry.input
class UpdateAdsInput:
    id: strawberry.ID  
    title: str = strawberry.UNSET
    img: str = strawberry.UNSET
    link: str = strawberry.UNSET
    status: bool = strawberry.UNSET
