from flask import request, Response, jsonify
from bson import json_util, ObjectId
from config.mongodb import mongo
from bson.json_util import dumps
import json
from models.ads import  AdsModels
from services.vacc import  get_vaccine_service 
from repository.planVaccineDependent import create_planVaccineDependent_repo, get_planVaccineDependentById_repo,get_planVaccineDependent_counts_repo
from repository.planVaccineDependent import delete_planVaccineDependent_repo, get_planVaccineDependentById_repo, find_one_applyVaccine_repo, get_planVaccineDependentList_repo
from repository.vacc import  get_vaccine_repo
from helps.utils import validar_object_id

"""Registro de """
    
def create_planVaccineDependent_service(data):
    status =  True
    if data:
        data['status'] = True
        response = create_planVaccineDependent_repo(data)
        
        result = {
                "id": str(response),
            }
        return result
    else:
        return "Invalid payload", 400

 


"""Obtiene las """


def get_planVaccineDependentList_service(limite, desde):
    limite = int(limite)
    desde = int(desde)
    data = get_planVaccineDependentList_repo(limite, desde)
    result = json_util.dumps(data)
    total = get_planVaccineDependent_counts_repo()
    diccionario = {
        'total': total,
        'limite':limite,
        'desde':desde,
        'planVaccineDependent': json.loads(result)
    }
    return jsonify((diccionario))

def get_planVaccineDependentbyId_service(id):
    data = get_planVaccineDependentById_repo(id)
    response_data = {
            'result': data,
    }
    response = Response(json.dumps(json.loads(json_util.dumps(response_data))), status=200, mimetype='application/json')
    return response

"""Obtener """

def get_planVaccineDependentBYIDservice(id):
    data = get_planVaccineDependentById_repo(id)
    response_data = {
            'result': data,
    }
    response = Response(json.dumps(json.loads(json_util.dumps(response_data))), status=200, mimetype='application/json')
    return response
    


 

 


"""Eliminar una vacuna"""


def delete_planVaccineDependent_service(id):
    data = get_planVaccineDependentById_repo(id)
    if data is not None:
        response =delete_planVaccineDependent_repo(id)
        if response.deleted_count >= 1:
            response = {
                'statusCode': 201,
                "resp": True,
                "message": "La planVaccineDependent ha sido eliminada correctamente" 
            }
            
            return response
        else:
            response = {
                'statusCode': 201,
                "resp": False,
                "message": "La planVaccineDependent no fue encontrada"
            }
            return response
    else:
         response = {
                'statusCode': 201,
                "resp": False,
                "message": "No existe registro para el id:"+id
         }
         return response 

def delete_planVaccineDep_service(id):
    data = get_planVaccineDependentById_repo(id)
    if data is not None:
        response =delete_planVaccineDependent_repo(id)
        if response.deleted_count >= 1:
            response = {
                'statusCode': 201,
                "resp": True,
                "message": "La planVaccineDependent ha sido eliminada correctamente" 
            }
            
            return response
        else:
            response = {
                'statusCode': 201,
                "resp": False,
                "message": "La planVaccineDependent no fue encontrada"
            }
            return response
    else:
         response = {
                'statusCode': 201,
                "resp": False,
                "message": "No existe registro para el id:"+id
         }
         return response 
