from flask import Flask, request, jsonify,  request, Response
import json
from bson.objectid import ObjectId
from config.mongodb import mongo
from bson import ObjectId
from models.schemaVaccineDosisDependents import SchemaVaccineDosisDependentsModels
from helps.utils import validar_object_id

def create_schemaVaccineDosisDependents_repo(obj:SchemaVaccineDosisDependentsModels):
    return mongo.db.schemaVaccineDosisDependents.insert_one(obj).inserted_id



def get_schemaVaccineDosisDependentsList_repo(limite:int, desde:int):
    query = {}  # Inicializar una consulta vacía
    
    return mongo.db.schemaVaccineDosisDependents.find(query).skip(desde).limit(limite)

def get_schemaVaccineDosisDependent_counts_repo():
     query = {}  # Inicializar una consulta vacía
    
     return mongo.db.schemaVaccineDosisDependents.count_documents(query)

def schemaVaccineDosisDependentById_repo(id):
    if validar_object_id(id):
        # La cadena es un ObjectId válido
        # Realiza las operaciones necesarias
        query = {"dependent_id": id}  # Construir la consulta para filtrar por dependent_id
        return mongo.db.schemaVaccineDosisDependents.find(query)
    else:
        # Maneja el error o muestra un mensaje de error
        result = {
             "TypeError": id,
             "ValueError": "La cadena no es un ObjectId válido" 
        }
        return result

def update_schemaVaccineDosisDependent_repo(id, data):
    if validar_object_id(id):
        # La cadena es un ObjectId válido
        # Realiza las operaciones necesarias
        return mongo.db.schemaVaccineDosisDependents.update_one({"_id":{'$eq': ObjectId(id)}}, {"$set": data})
    else:
        # Maneja el error o muestra un mensaje de error
        result = {
             "TypeError": id,
             "ValueError": "La cadena no es un ObjectId válido" 
        }
        return result        

 
def find_one_schemaVaccineIdDosisIdDependents_repo(dosis_id, idDependent):
    filter_query = {
        'status': {'$in': [True, 'True', 'true']},
        'dosis_id': dosis_id,
        'dependent_id': idDependent
    }
    return mongo.db.schemaVaccineDosisDependents.find(filter_query)

def delete_schemaVaccineDosisDependent_repo(id: str):
    query = {"_id": ObjectId(id)} # Construir la consulta para filtrar por dependent_id
    result = mongo.db.schemaVaccineDosisDependents.delete_one(query)
    return result  # Devolver la cantidad de documentos eliminados


def find_one_schemaVaccineDosisDependents_repo(query):     
    return mongo.db.schemaVaccineDosisDependents.find_one(query)

def find_one_repo(query):     
    return mongo.schemaVaccineDosisDependents.ads.find_one(query)

def isValidBdplanVaccineDependent(title):
    
    return {"resp":True}


def isValidBdschemaVaccineDosisDependentsUpdate(id, data):

    return {"resp":True}
     
    #




    
