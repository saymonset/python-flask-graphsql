import json
import strawberry
from typing import List
@strawberry.type(description="Agregations ")
class AggregationsType:
    total: int;
    deleteds: int;
    actives: int;
