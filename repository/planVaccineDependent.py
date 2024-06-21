from flask import Flask, request, jsonify,  request, Response
import json
from bson.objectid import ObjectId
from config.mongodb import mongo
from bson import ObjectId
from models.planVaccineDependent import PlanVaccineDependentModels
from helps.utils import validar_object_id

def create_planVaccineDependent_repo(obj:PlanVaccineDependentModels):
    return mongo.db.planVaccineDependent.insert_one(obj).inserted_id



def get_planVaccineDependentList_repo(limite:int, desde:int):
    query = {}  # Inicializar una consulta vacía
    
    return mongo.db.planVaccineDependent.find(query).skip(desde).limit(limite)

def get_planVaccineDependent_counts_repo():
     query = {}  # Inicializar una consulta vacía
    
     return mongo.db.planVaccineDependent.count_documents(query)

def get_planVaccineDependentById_repo(id):
    if validar_object_id(id):
        # La cadena es un ObjectId válido
        # Realiza las operaciones necesarias
        query = {"dependent_id": id}  # Construir la consulta para filtrar por dependent_id
        return mongo.db.planVaccineDependent.find(query)
    else:
        # Maneja el error o muestra un mensaje de error
        result = {
             "TypeError": id,
             "ValueError": "La cadena no es un ObjectId válido" 
        }
        return result

 

def delete_planVaccineDependent_repo(dependent_id: str):
    query = {"dependent_id": dependent_id}  # Construir la consulta para filtrar por dependent_id
    result = mongo.db.planVaccineDependent.delete_many(query)  # Utilizar delete_many para eliminar todos los documentos que coincidan con la consulta
    return result  # Devolver la cantidad de documentos eliminados


def find_one_applyVaccine_repo(query):     
    return mongo.db.planVaccineDependent.find_one(query)

def find_one_repo(query):     
    return mongo.planVaccineDependent.ads.find_one(query)

def isValidBdplanVaccineDependent(title):
    
    return {"resp":True}


def isValidBdplanVaccineDependentUpdate(id, data):
    title = data.get("title")
    query = {'title': title, '_id': {'$ne': ObjectId(id)}}
    objs = find_one_repo(query)
    if objs:
        return {"resp":False,
                "name":"planVaccineDependent exist en bd"}
    
    return {"resp":True}
    #




    
