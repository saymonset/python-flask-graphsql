from flask import request, Response, jsonify
from bson import json_util, ObjectId
from config.mongodb import mongo
from bson.json_util import dumps
import json
from models.ads import  AdsModels
from services.vacc import  get_vaccine_service 
from repository.ads import update_applyVaccine_repo, create_ads_repo, get_adsById_repo,get_ads_counts_repo
from repository.ads import delete_ads_repo, get_adsById_repo, find_one_applyVaccine_repo, get_adsList_repo, \
get_adsById_repo, get_adsList_status_repo, get_ads_totales_counts_repo, get_ads_totales_counts_repo, get_ads_deletes_counts_repo
from repository.vacc import  get_vaccine_repo
from helps.utils import validar_object_id
from dto.inputs.create_ads_input import CreateAdsInput
from dto.inputs.update_ads_input import UpdateAdsInput
from models.ads import AdsModels
from dto.args.status_args import  StatusASrgs
 
"""Obtiene las ads"""
def get_adsList_GRPHQL_Statusservice(statusArgs: StatusASrgs):
    return get_adsList_status_repo(statusArgs)

"""Obtiene las ads"""
def get_adsList_GRPHQLservice(limite, desde):
    return get_adsList_repo(limite, desde)

"""Obtiene los totales"""
def get_totalads_GRPHQLservice():
    return get_ads_totales_counts_repo()

"""Obtiene los activos"""
def get_totalActivosads_GRPHQLservice():
    return get_ads_counts_repo()

"""Obtiene los deletes"""
def get_totalDeletessads_GRPHQLservice():
    return get_ads_deletes_counts_repo()


"""Obtener una ads"""
def get_adsbyId_GRPHQL_service(id):
    result = get_adsById_repo(id)
    if result is None:
        return "El id no se encuentra"
    else:
        return result

"""Registro de vacunas"""
    
def create_ads_GRAPHQL_service(data:CreateAdsInput):
       # data['status'] = True
        response = create_ads_repo(AdsModels(title=data.title, img=data.img, link=data.link, status=data.status))
     
        return AdsModels(title=data.title, img=data.img, link=data.link, status=data.status)


def update_ads_GRAPHQL_service(data:UpdateAdsInput):
       # data['status'] = True
        response = update_applyVaccine_repo(data.id, data)
        
        return AdsModels(title=data.title, img=data.img, link=data.link, status=data.status)

def delete_ads_GRAPHQL_service(id:str):
        #Si existre , no da error
        response = get_adsById_repo(id)
        #Lo puedes borrar , lo borramos
        responseII = delete_ads_repo(id)
        return True
 