import strawberry
from typing import Optional

@strawberry.input
class SendPhoneInput:
    phone: str

    def get(self, attribute: str) -> Optional[str]:
        """
        Custom method to retrieve attribute values based on the attribute name.
        """
        if hasattr(self, attribute):
            return getattr(self, attribute)
        else:
            return None
