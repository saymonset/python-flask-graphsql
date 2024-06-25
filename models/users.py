import strawberry
from typing import List, Optional
import json
@strawberry.type
class UserModels:
    id: strawberry.ID = strawberry.UNSET
    phone:str  = strawberry.UNSET
    lastCode:str = strawberry.UNSET
    token:str = strawberry.UNSET
    birth:str = strawberry.UNSET
    ci:str = strawberry.UNSET
    city:str = strawberry.UNSET
    email:str = strawberry.UNSET
    genderId:str = strawberry.UNSET
    lastname:str = strawberry.UNSET
    name:str = strawberry.UNSET
    password:str = strawberry.UNSET
    state:str = strawberry.UNSET
    status:str = strawberry.UNSET
    isActive:bool = strawberry.UNSET
    roles: List[str] = strawberry.UNSET
   
   
 


 