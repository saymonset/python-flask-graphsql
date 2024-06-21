from flask import request, Response, jsonify
from bson import json_util, ObjectId
from config.mongodb import mongo
from bson.json_util import dumps
import json
from models.ads import  AdsModels
from services.vacc import  get_vaccine_service 
from repository.imageByDosisDependent import create_imageByDosisDependent_repo, get_imageByDosisDependentById_repo,get_imageByDosisDependent_counts_repo
from repository.imageByDosisDependent import delete_imageByDosisDependent_repo, find_one_applyVaccine_repo, get_imageByDosisDependentList_repo
from repository.vacc import  get_vaccine_repo
from helps.utils import validar_object_id

"""Registro de """
    
def create_imageByDosisDependent_service(data):
    status =  True
    if data:
        data['status'] = True
        response = create_imageByDosisDependent_repo(data)
        
        result = {
                "id": str(response),
            }
        return result
    else:
        return "Invalid payload", 400

 


"""Obtiene las """

 

 

"""Obtener """

def get_imageByDosisDependentBYIDservice(dependent_id, dosis_id):
    data = get_imageByDosisDependentById_repo(dependent_id, dosis_id)
    response_data = {
            'result': data,
    }
    response = Response(json.dumps(json.loads(json_util.dumps(response_data))), status=200, mimetype='application/json')
    return response
    


 

 


"""Eliminar una vacuna"""

 

def delete_imageByDosisDependent_service(dependent_id, dosis_id):
    data = get_imageByDosisDependentById_repo(dependent_id, dosis_id)
    if data is not None:
        response =delete_imageByDosisDependent_repo(dependent_id, dosis_id)
        if response.deleted_count >= 1:
            response = {
                'statusCode': 201,
                "resp": True,
                "message": "La imageByDosisDependent ha sido eliminada correctamente" 
            }
            
            return response
        else:
            response = {
                'statusCode': 201,
                "resp": False,
                "message": "La imageByDosisDependent no fue encontrada"
            }
            return response
    else:
         response = {
                'statusCode': 201,
                "resp": False,
                "message": "No existe registro para el id:"+id
         }
         return response 
