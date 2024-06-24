import json
import strawberry
from typing import List
from typing import Optional
@strawberry.type
class AdsModels:
    id: strawberry.ID = strawberry.UNSET
    title:str
    img:str
    link:Optional[str]
    status:bool 
     


# import strawberry
# from typing import Optional

# @strawberry.type
# class Item:
#     id: strawberry.ID
#     name: str
#     quantity: float
#     quantityUnits: Optional[str]

# # Ejemplo de uso
# @strawberry.type
# class Query:
#     @strawberry.field
#     def get_item(self, item_id: strawberry.ID) -> Item:
#         # Lógica para obtener un ítem por su ID
#         return Item(id=item_id, name="Sample Item", quantity=10.5, quantityUnits="kg")

# schema = strawberry.Schema(query=Query)
