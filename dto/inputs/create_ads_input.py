import strawberry
from typing import Optional
@strawberry.input
class CreateAdsInput:
    title:str
    img:str
    link:str
    status:bool 
    # quantity: float
    #quantityUnits: Optional[str]