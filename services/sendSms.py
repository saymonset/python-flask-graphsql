from flask import request, Response, jsonify
from bson import json_util, ObjectId
from bson.json_util import dumps
import json
from models.users import UserModels
from config.mongodb  import   mongo
import random
import os
from pymongo import MongoClient
from twilio.rest import Client
import logging

from repository.user import   crear_users_repo, update_status_user_repo, get_phone_in_users_repo




"""Registro de objetos"""
 

def get_phone_in_users_service(phone):
   
    if phone:
        user =  get_phone_in_users_repo(phone)
        if user:
            return {
                  "error": False,
                  "statusCode": 200,
                  "resp": False,
                  "message": "El usuario existe"
                  }
        else:
            return {
                "error": False,
                "resp": True,
                "statusCode": 400,
                "message": "El usuario no existe",
            }    
    else:
            return {
                "error": True,
                "resp": True,
                "statusCode": 400,
                "message": "El telefono no existe",
            }

 

def sendSms_graphql_service(data):
    #Tomamos el telefono que se envia
    phone = data.get("phone")
    if phone:
        rand_num = random.randint(99999,999999)
        user =  get_phone_in_users_repo(phone)
        if user:
            #Si no tiene status el usuqariop, se coloca como unverified su status
            if 'status' not in user:
                data = {'status': 'unverified'}
                update_status_user_repo(user['_id'], data)
                user =  get_phone_in_users_repo(phone)
             #Si tiene como statu verified, se le manda de nuevo su codigo de tlf   
            if user['status'] == 'unverified':
                result = sendSms_phone(phone, rand_num)
                if not bool(result["resp"]):  return result 
                data = {'lastCode': rand_num}
                update_status_user_repo(user['_id'], data)
                response = {
                    "resp":True,
                    'statusCode': 201,
                    'lastCode':rand_num,
                    'message': "Code was sent successfully."
                }
            else:
                    #El usuqario pide que se le reenvie erl codigo nuevo porque ya esta verificado
                    result = sendSms_phone(phone, rand_num)
                    if not bool(result["resp"]):  return result 
                    
                    data = {'lastCode': rand_num}
                    update_status_user_repo(user['_id'], data)
                    response = {
                        "resp":True,
                        'statusCode': 201,
                         'lastCode':rand_num,
                        'message': "Code was sent successfully."
                    }
        else:    
            #Es primera ves refgistradose en el telefono
            result = sendSms_phone(phone, rand_num)
            if not bool(result["resp"]):  return result 
            
            # The `user` variable is used to store the result of the `get_phone_in_users_repo` function, which retrieves user data from the repository based on the provided phone number.
            user = {
                'phone': phone,
                'lastCode': rand_num,
                'status': 'unverified'
            }
        
                    
            crear_users_repo(user)
            #users.insert_one(user).inserted_id
            response = {
                "resp":True,
                 'lastCode':rand_num,
                'statusCode': 201,
                'message': 'Code was sent successfully.'
            }
        return response
    else:
        return "Invalid payload", 400
def sendSms_service(data):
    #Tomamos el telefono que se envia
    phone = data.get("phone")
    if phone:
        rand_num = random.randint(99999,999999)
        user =  get_phone_in_users_repo(phone)
        if user:
            #Si no tiene status el usuqariop, se coloca como unverified su status
            if 'status' not in user:
                data = {'status': 'unverified'}
                update_status_user_repo(user['_id'], data)
                user =  get_phone_in_users_repo(phone)
             #Si tiene como statu verified, se le manda de nuevo su codigo de tlf   
            if user['status'] == 'unverified':
                result = sendSms_phone(phone, rand_num)
                if not bool(result["resp"]):  return result 
                data = {'lastCode': rand_num}
                update_status_user_repo(user['_id'], data)
                response = {
                    "resp":True,
                    'statusCode': 201,
                    'lastCode':rand_num,
                    'message': "Code was sent successfully."
                }
            else:
                    #El usuqario pide que se le reenvie erl codigo nuevo porque ya esta verificado
                    result = sendSms_phone(phone, rand_num)
                    if not bool(result["resp"]):  return result 
                    
                    data = {'lastCode': rand_num}
                    update_status_user_repo(user['_id'], data)
                    response = {
                        "resp":True,
                        'statusCode': 201,
                         'lastCode':rand_num,
                        'message': "Code was sent successfully."
                    }
        else:    
            #Es primera ves refgistradose en el telefono
            result = sendSms_phone(phone, rand_num)
            if not bool(result["resp"]):  return result 
            
            # The `user` variable is used to store the result of the `get_phone_in_users_repo` function, which retrieves user data from the repository based on the provided phone number.
            user = {
                'phone': phone,
                'lastCode': rand_num,
                'status': 'unverified'
            }
        
                    
            crear_users_repo(user)
            #users.insert_one(user).inserted_id
            response = {
                "resp":True,
                 'lastCode':rand_num,
                'statusCode': 201,
                'message': 'Code was sent successfully.'
            }
        return response
    else:
        return "Invalid payload", 400


def sendSms_phone(phone, rand_num):
    try:
        # print('TWILIO_ID=AC4a08804ab190c961da30f7128652cf7c = '+TWILIO_ID)
        # print('TWILIO_AUTH_TOKEN= d15f0cb126787f66cbc0cec2cd7b25c1 '+TWILIO_AUTH_TOKEN)
        # print('TWILIO_PHONE= +12255358206 = '+TWILIO_PHONE)

        account_sid = 'AC4a08804ab190c961da30f7128652cf7c'#os.environ.get('TWILIO_ID')
        auth_token = 'd15f0cb126787f66cbc0cec2cd7b25c1'#os.environ.get('TWILIO_AUTH_TOKEN')
        client = Client(account_sid, auth_token)
        client.messages.create(
                        #from_=os.environ.get('TWILIO_PHONE'),
                        from_='+12255358206',
                        body=f"Your validation code is: {rand_num}",
                        to=phone
                    )
        resp = {"resp":True,
                "statusCode": 201,
                "lastCode": '',
                "message": " successfully."
               }
        return resp
    except Exception as e:
	
        resp =    {"resp":False,
                    "statusCode": 501,
                    "lastCode":'',
                    "error":"Hubo un error al mandar el mensaje, por favor intente nuevamente.",
                    "message":"Hubo un error al mandar el mensaje, por favor intente nuevamente."}
                    #CUANDO FUNCIONE TWILIO, COMENTAR EL BLOQUE SIGUIENTE
        resp =    {"resp":True,
                    "statusCode": 501,
                    "lastCode":'',
                    "error":"Temporal envio de sms. Esta hardoCode!",
                    "message":"Temporal envio de sms. Esta hardoCode!"}
        return resp
 
