import strawberry
from typing import List, Optional
import json
@strawberry.type
class UserModels:
    id: strawberry.ID = strawberry.UNSET
    phone:str  = strawberry.UNSET
    last_code:str = strawberry.UNSET
    token:str = strawberry.UNSET
    birth:str = strawberry.UNSET
    ci:str = strawberry.UNSET
    city:str = strawberry.UNSET
    email:str = strawberry.UNSET
    gender:str = strawberry.UNSET
    lastname:str = strawberry.UNSET
    name:str = strawberry.UNSET
    password:str = strawberry.UNSET
    state:str = strawberry.UNSET
    status:bool = strawberry.UNSET
    roles: List[str] = strawberry.UNSET
   
   

# class UserModels:
#     def __init__(self 
                 
#                  ):
#         self.phone = phone
#         self.last_code = last_code
#         self.status = status
#         self.token=token
#         self.birth=birth
#         self.ci=ci
#         self.city=city
#         self.email=email
#         self.gender=gender
#         self.lastname=lastname
#         self.password=password
#         self.state=state


 