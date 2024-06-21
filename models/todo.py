import json
class TodoModels:
    def __init__(self, 
                 description:str, 
                 done:bool 
                 ):
        self.description = description
        self.done = done