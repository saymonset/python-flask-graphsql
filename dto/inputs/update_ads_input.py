import strawberry

@strawberry.input
class UpdateAdsInput:
    idAds: str
    title: str = strawberry.UNSET
    img: str = strawberry.UNSET
    link: str = strawberry.UNSET
    status: bool = strawberry.UNSET
