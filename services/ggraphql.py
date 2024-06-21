from flask import request, Response, jsonify
# from ariadne import load_schema_from_path, make_executable_schema, \
#     graphql_sync, snake_case_fallback_resolvers, ObjectType
#from ariadne.explorer import ExplorerGraphiQL
 
from flask import request, jsonify
from bson import json_util, ObjectId
from config.mongodb import mongo
from bson.json_util import dumps
import json
from models.ads import  AdsModels
from services.vacc import  get_vaccine_service 
from repository.ads import update_applyVaccine_repo, create_ads_repo, get_adsById_repo,get_ads_counts_repo
from repository.ads import delete_ads_repo, get_adsById_repo, find_one_applyVaccine_repo, get_adsList_repo
from repository.vacc import  get_vaccine_repo
from helps.utils import validar_object_id

#from graphql.queries import resolve_todos



 


def get_adsbyId_service():
    print("------------a------------------")
    
    print("------------b------------------")
  
    response_data = {
            'resultgggg': 'ok',
    }
    response = Response(json.dumps(json.loads(json_util.dumps(response_data))), status=200, mimetype='application/json')
    return response


"""Actualizacion de vacuna"""


def update_ads_service(id, data):
    if len(data) == 0:
        return "No hay datos para actualizar", 400

    if validar_object_id(id):
        # La cadena es un ObjectId válido
        # Realiza las operaciones necesarias
        response = update_applyVaccine_repo(id, data)
        if response.modified_count >= 1:
            return "La ads ah sido actualizada correctamente", 200
        else:
            return "La ads no fue modificada", 404
    else:
        # Maneja el error o muestra un mensaje de error
        result = {
             "TypeError": id,
             "ValueError": "La cadena no es un ObjectId válido" 
        }
        return result    

 


"""Eliminar una vacuna"""


def delete_ads_service(id):
    data = get_adsById_repo(id)
    if data is not None:
        response =delete_ads_repo(id)
        if response.deleted_count >= 1:
            return "La ads ha sido eliminada correctamente", 200
        else:
            return "La ads no fue encontrada", 404
    else:
         return "No existe registro para el id:"+id, 400       
