import json
import strawberry
from typing import List
from typing import Optional
@strawberry.type
class SendPhoneResponse:
    resp:str
    statusCode:str
    message:str 
    lastCode:str  = strawberry.UNSET
    error:str = strawberry.UNSET
    token:str = strawberry.UNSET