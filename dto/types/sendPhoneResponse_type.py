import strawberry
from typing import List, Optional

@strawberry.type
class SendPhoneResponse:
    resp: Optional[str] = None
    statusCode: Optional[str] = None
    message: Optional[str] = None
    lastCode: Optional[str] = None
    error: Optional[str] = None
    token: Optional[str] = None
    Token: Optional[str] = None
    usuario: Optional[str] = None
    user_id: Optional[str] = None



 