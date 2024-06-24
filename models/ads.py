import json
import strawberry
from typing import List
@strawberry.type
class AdsModels:
    id:  str  = strawberry.UNSET
    title:str
    img:str
    link:str
    status:bool 