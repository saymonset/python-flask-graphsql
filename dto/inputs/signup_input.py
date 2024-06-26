import strawberry
from typing import Optional

@strawberry.input
class SignUpInput:
    name: str
    lastname: str
    password: str
    ci: str
    email: str
    state: str
    city: str
    birth: str
    genderId: str
    status: bool
 

    def get(self, attribute: str) -> Optional[str]:
        """
        Custom method to retrieve attribute values based on the attribute name.
        """
        return getattr(self, attribute, None)

