import json
from datetime import date
class SchemaVaccineDosisDependentsModels:
    def __init__(self, dosis_id:str, 
                       vaccine_id:str, 
                       dependent_id:str,  
                       expires_in_days: int,
                       date_must_apply: str,
                       isApplied:bool,
                       status:bool):
        self.dosis_id = dosis_id
        self.vaccine_id = vaccine_id
        self.dependent_id = dependent_id
        self.expires_in_days = expires_in_days
        self.date_must_apply = date_must_apply
        self.isApplied = isApplied
        self.status = status