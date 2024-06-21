from flask import Flask, request, jsonify,  request, Response
import json
from bson.objectid import ObjectId
from config.mongodb import mongo
from bson import ObjectId
from models.imageByDosisDependent import ImageByDosisDependenttModels
from helps.utils import validar_object_id

def create_imageByDosisDependent_repo(obj:ImageByDosisDependenttModels):
    return mongo.db.imageByDosisDependent.insert_one(obj).inserted_id



def get_imageByDosisDependentList_repo(limite:int, desde:int):
    query = {}  # Inicializar una consulta vacía
    
    return mongo.db.imageByDosisDependent.find(query).skip(desde).limit(limite)

def get_imageByDosisDependent_counts_repo():
     query = {}  # Inicializar una consulta vacía
    
     return mongo.db.imageByDosisDependent.count_documents(query)

def get_imageByDosisDependentById_repo(dependent_id, dosis_id):
    if validar_object_id(dependent_id):
        # La cadena es un ObjectId válido
        # Realiza las operaciones necesarias
        query = {"dependent_id": dependent_id, "dosis_id": dosis_id} 
        return mongo.db.imageByDosisDependent.find(query)
    else:
        # Maneja el error o muestra un mensaje de error
        result = {
             "TypeError": id,
             "ValueError": "La cadena no es un ObjectId válido" 
        }
        return result

 

def delete_imageByDosisDependent_repo(dependent_id: str, dosis_id:str):
    query = {"dependent_id": dependent_id, "dosis_id": dosis_id}   # Construir la consulta para filtrar por dependent_id
    result = mongo.db.imageByDosisDependent.delete_many(query)  # Utilizar delete_many para eliminar todos los documentos que coincidan con la consulta
    return result  # Devolver la cantidad de documentos eliminados


def find_one_applyVaccine_repo(query):     
    return mongo.db.imageByDosisDependent.find_one(query)

def find_one_repo(query):     
    return mongo.imageByDosisDependent.ads.find_one(query)

def isValidBdimageByDosisDependent(title):
    
    return {"resp":True}


def isValidBdimageByDosisDependentUpdate(id, data):
    title = data.get("title")
    query = {'title': title, '_id': {'$ne': ObjectId(id)}}
    objs = find_one_repo(query)
    if objs:
        return {"resp":False,
                "name":"imageByDosisDependent exist en bd"}
    
    return {"resp":True}
    #




    
