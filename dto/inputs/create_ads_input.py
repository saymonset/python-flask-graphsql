import strawberry

@strawberry.input
class CreateAdsInput:
    title:str
    img:str
    link:str
    status:bool 