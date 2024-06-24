import json
import strawberry
from typing import List
@strawberry.type
class AggregationsType:
    total: int;
    deleteds: int;
    actives: int;