import json
import strawberry
from typing import List
from typing import Optional
@strawberry.type
class SendPhoneResponse:
    resp:str
    lastCode:str
    statusCode:str
    message:str 
    error:str = strawberry.UNSET