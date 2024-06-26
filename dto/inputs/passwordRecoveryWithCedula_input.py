import strawberry
from typing import Optional

@strawberry.input
class PasswordRecoveryWithCedulaInput:
    phone: str
    ci: str

    def get(self, attribute: str) -> Optional[str]:
        """
        Custom method to retrieve attribute values based on the attribute name.
        """
        return getattr(self, attribute, None)

