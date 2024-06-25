import json
from datetime import datetime

class DependentModels:
    def __init__(self, 
                 phone:str, 
                 lastCode:str,
                 status:bool,
                 token:str,
                 birth:str,
                 ci:str,
                 city:str,
                 email:str,
                 gender:str,
                 lastname:str,
                 name:str,
                 password:str,
                 state:str
                 ):
        self.phone = phone
        self.lastCode = lastCode
        self.status = status
        self.token=token
        self.birth=birth
        self.ci=ci
        self.city=city
        self.email=email
        self.gender=gender
        self.lastname=lastname
        self.password=password
        self.state=state


 