from flask import Flask, request, jsonify,  request, Response
import json
from bson.objectid import ObjectId
from config.mongodb import mongo
from models.dependent import DependentModels
from bson import ObjectId
from models.specialities import SpecialitiesModels
from models.doctors import  DoctorsModels
from helps.utils import validar_object_id, get_caracteres_especiales
import re


 

 
def checkUserDependent(query):     
    #La primera ves se usa la colletion users y no dependents
    return mongo.db.dependents.find_one(query)

 
def get_dependentById_repo(id):
    if validar_object_id(id):
        # La cadena es un ObjectId válido
        # Realiza las operaciones necesarias
        return mongo.db.dependents.find_one({"_id": ObjectId(id)})
    else:
            # Maneja el error o muestra un mensaje de error
        result  = {
                "error":False,
                "resp":False,
                "TypeError": id,
                "statusCode": "badCadena",
                "ValueError": "La cadena no es un ObjectId válido" ,
                "message": "La cadena no es un ObjectId válido" 
         }

        #   {
        #         'resp':True,
        #         'statusCode': 200,
        #         'message' : "Code was checked successfully. Proceed with registration", 
        #         'token': token
        #     }
        return result

def get_dependentByIdFillAll_repo(id):
    if validar_object_id(id):
        # La cadena es un ObjectId válido
        # Realiza las operaciones necesarias
        result = mongo.db.dependents.find_one({"_id": ObjectId(id)})

        return result
    else:
            # Maneja el error o muestra un mensaje de error
        result  = {
                "error":False,
                "resp":False,
                "TypeError": id,
                "ValueError": "La cadena no es un ObjectId válido" 
         }
        return result

def delete_dependent_repo(id):
         #return mongo.db.dependents.delete_one({"_id": ObjectId(id)})
         return mongo.db.dependents.update_one({"_id": ObjectId(id)}, {"$set": {"status": False}})   

def update_dependent_status(id):
    return mongo.db.dependents.update_one({"_id": ObjectId(id)}, {"$set": {"status": False}})   

def crear_dependents_repo(obj:DependentModels):
    obj['status']=True
    return mongo.db.dependents.insert_one(obj).inserted_id

def get_dependents_repo(limite:int, desde:int, user_id, query):
    contador = get_caracteres_especiales(query)

    if query is not None and (not query.strip() or len(query) == contador):
        filter_query = {
            'status': {'$in': [True, 'True', 'true']},
            '$or': [
                {'user_id': ObjectId(user_id)},
                {'user_id': user_id}
            ]
        }
    else:
        filter_query = {
            "$or": [
                {"name": {"$regex": query, "$options": "i"}},
                {"lastname": {"$regex": query, "$options": "i"}}
            ]
        }

    return mongo.db.dependents.find(filter_query).skip(desde).limit(limite)

def get_dependentsWithoutFilter_repo():
    filter_query = {
        'status': {'$in': [True, 'True', 'true']}
    }

    return mongo.db.dependents.find(filter_query)

def get_dependents_counts_repo(user_id, query:str):
    contador = get_caracteres_especiales(query)

    if query is not None and (not query.strip() or len(query) == contador):
        filter_query = {
            'status': {'$in': [True, 'True', 'true']},
            '$or': [
                {'user_id': ObjectId(user_id)},
                {'user_id': user_id}
            ]
        }
    else:
        filter_query = {
            "$or": [
                {"name": {"$regex": query, "$options": "i"}},
                {"lastname": {"$regex": query, "$options": "i"}}
            ]
        }

    return mongo.db.dependents.count_documents(filter_query)





def update_dependents_repo(id, data):
    if validar_object_id(id):
        # La cadena es un ObjectId válido
        # Realiza las operaciones necesarias
        return mongo.db.dependents.update_one({"_id":{'$eq': ObjectId(id)}}, {"$set": data})
    else:
        # Maneja el error o muestra un mensaje de error
        result = {
             "TypeError": id,
             "ValueError": "La cadena no es un ObjectId válido" 
        }
        return result