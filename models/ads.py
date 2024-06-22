import json
import strawberry
from typing import List
# class AdsModels:
#     def __init__(self, 
#                  title:str, 
#                  img:str,
#                  link:str,
#                  status:bool 
#                  ):
#         self.img = img
#         self.link = link
#         self.status = status

@strawberry.type
class AdsModels:
    title:str
    img:str
    link:str
    status:bool 