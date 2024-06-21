from flask import request, Response, jsonify
from bson import json_util, ObjectId
from config.mongodb import mongo
from bson.json_util import dumps
import json
from models.ads import  AdsModels
from services.vacc import  get_vaccine_service 
from repository.dosis import  get_dosisWithoutFilter_repo 
from repository.schemaVaccineDosisDependents import create_schemaVaccineDosisDependents_repo, schemaVaccineDosisDependentById_repo,get_schemaVaccineDosisDependent_counts_repo, update_schemaVaccineDosisDependent_repo
from repository.schemaVaccineDosisDependents import find_one_schemaVaccineIdDosisIdDependents_repo, delete_schemaVaccineDosisDependent_repo, schemaVaccineDosisDependentById_repo, find_one_schemaVaccineDosisDependents_repo, get_schemaVaccineDosisDependentsList_repo
from repository.vacc import  get_vaccine_repo
from repository.dependent import  get_dependentsWithoutFilter_repo
from repository.applyVaccines import get_apply__vaccineOfDosisAndDependent_repo
from helps.utils import validar_object_id
from validators.utils import calcular_edad_y_es_nino, calcular_date_must_apply

"""Registro de """
    
def create_schemaVaccineDosisDependents_service(data):
    status =  True
    if data:
        data['status'] = True
        response = create_schemaVaccineDosisDependents_repo(data)
        
        result = {
                "id": str(response),
            }
        return result
    else:
        return "Invalid payload", 400

def crea_schemaVaccineDosisDependentsLoad(dependent_id, birth, dosis_id, vacinne_id, expires_in_days):
        date_must_apply = calcular_date_must_apply(birth, expires_in_days);
        
        isApplied = False
        data = {
            'dependent_id': str(dependent_id),
            'dosis_id': str(dosis_id),
            'vacinne_id': vacinne_id,
            'date_must_apply': date_must_apply,
            'expires_in_days': expires_in_days,
            'isApplied': isApplied,
            'status':True
        }

        #print(data)
        print('Dosis: {}'.format(dosis_id))
        print('dependent_id: {}'.format(dependent_id))

        existeSchemaVaccineIdDosisIdDependents = find_one_schemaVaccineIdDosisIdDependents_repo(str(dosis_id), str(dependent_id))
        
        # Obtener el primer elemento del cursor
        primer_elemento = next(existeSchemaVaccineIdDosisIdDependents, None)
        print(primer_elemento)
        # Verificar si el cursor está vacío
        if primer_elemento is not None:
            dataAppliedInDosisDependent = get_apply__vaccineOfDosisAndDependent_repo(dosis_id, dependent_id)
            schema_id = primer_elemento['_id']  

            if dataAppliedInDosisDependent is None: 
                isApplied = False
            else: 
                isApplied = True
                data['isApplied'] = isApplied
                
            update_schemaVaccineDosisDependent_repo(schema_id, data)

             
            print('------------------------')
            print(schema_id)
            print('------------------------')
             
             
            print('Update')
        else:
            #print('Create')
            create_schemaVaccineDosisDependents_repo(data)
            
            # print(dependent_id)

            
        # print(dosis_id)
        # print(vacinne_id) 
        # print(expires_in_days)
        return "ok"

def get_schemaVaccineDosisDependentsLoad_service():

    #Sacamos ALL Dependents en BD
    dataDependent = get_dependentsWithoutFilter_repo(); 
    for dependent in dataDependent:
        #Recuperamos la data de la dosis
        dependent_id = dependent['_id']
        birth = dependent['birth']
        #Sacamos todas las dosis en BD
        dosisData = get_dosisWithoutFilter_repo()
        for dosis in dosisData:
            dosis_id = dosis['_id']
            vacinne_id = dosis['vacinne_id']
            expires_in_days = dosis['expires_in_days']
            crea_schemaVaccineDosisDependentsLoad(dependent_id, birth, dosis_id, vacinne_id, expires_in_days);

    result = json_util.dumps(dataDependent)
    diccionario = {
        'total': 'total',
        'limite':'limite',
        'desde':'desde',
        'dependets': json.loads(result)
    }
  
    return jsonify((diccionario))

"""Obtiene las """


def get_schemaVaccineDosisDependentsList_service(limite, desde):
    limite = int(limite)
    desde = int(desde)
    data = get_schemaVaccineDosisDependentsList_repo(limite, desde)
    result = json_util.dumps(data)
    total = get_schemaVaccineDosisDependent_counts_repo()
    diccionario = {
        'total': total,
        'limite':limite,
        'desde':desde,
        'schemaVaccineDosisDependents': json.loads(result)
    }
    return jsonify((diccionario))

# def create_schemaVaccineDosisDependents_service(id):
#     data = schemaVaccineDosisDependentById_repo(id)
#     response_data = {
#             'result': data,
#     }
#     response = Response(json.dumps(json.loads(json_util.dumps(response_data))), status=200, mimetype='application/json')
#     return response

"""Obtener """

def get_schemaVaccineDosisDependentBYIDservice(id):
    data = schemaVaccineDosisDependentById_repo(id)
    response_data = {
            'result': data,
    }
    response = Response(json.dumps(json.loads(json_util.dumps(response_data))), status=200, mimetype='application/json')
    return response

def get_schemaVaccineIdDosisIdDependentsservice(dosis_id, idDependent):
    data = find_one_schemaVaccineIdDosisIdDependents_repo(dosis_id, idDependent)
    response_data = {
            'result': data,
    }
    response = Response(json.dumps(json.loads(json_util.dumps(response_data))), status=200, mimetype='application/json')
    return response
    


 

"""Actualizacion de vacuna"""


def update_schemaVaccineDosisDependent_service(id, data):
    if len(data) == 0:
        return "No hay datos para actualizar", 400

    if validar_object_id(id):
        # La cadena es un ObjectId válido
        # Realiza las operaciones necesarias
        response = update_schemaVaccineDosisDependent_repo(id, data)
        if response.modified_count >= 1:
            result = {
                "message":"La schemaVaccineDosisDependent ha sido actualizada correctamente", 
                "statusCode": 200,
                 "resp":True,
            }
            return result
        else:
            result = {
                "message":"La schemaVaccineDosisDependent no fue encontrada", 
                "statusCode": 404,
                 "resp":False,
            }
            return result
    else:
        # Maneja el error o muestra un mensaje de error
        result = {
                "TypeError": id,
                "ValueError": "La cadena no es un ObjectId válido" ,
                "message":"La cadena no es un ObjectId válido", 
                "statusCode": 404,
                 "resp":False,
            }
        return result   


"""Eliminar una vacuna"""


def delete_planVaccineDependent_service(id):
    data = schemaVaccineDosisDependentById_repo(id)
    if data is not None:
        response =delete_schemaVaccineDosisDependent_repo(id)
        if response.deleted_count >= 1:
            response = {
                'statusCode': 201,
                "resp": True,
                "message": "La schemaVaccineDosisDependent ha sido eliminada correctamente" 
            }
            
            return response
        else:
            response = {
                'statusCode': 201,
                "resp": False,
                "message": "La schemaVaccineDosisDependent no fue encontrada"
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
    data = schemaVaccineDosisDependentById_repo(id)
    if data is not None:
        response =delete_schemaVaccineDosisDependent_repo(id)
        if response.deleted_count >= 1:
            response = {
                'statusCode': 201,
                "resp": True,
                "message": "La schemaVaccineDosisDependent ha sido eliminada correctamente" 
            }
            
            return response
        else:
            response = {
                'statusCode': 201,
                "resp": False,
                "message": "La schemaVaccineDosisDependent no fue encontrada"
            }
            return response
    else:
         response = {
                'statusCode': 201,
                "resp": False,
                "message": "No existe registro para el id:"+id
         }
         return response 
