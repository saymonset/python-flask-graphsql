import strawberry
from typing import List, Optional
from flask_jwt_extended import jwt_required, get_jwt_identity

import random
from typing import Optional
from services.user import get_users_GRPHQL_Statusservice, get_userbyIdRaw_service
from services.sendSms import sendSms_graphql_service
from services.checkCode import checkCode_service_graphql, check_CI_service_graphql
from services.user import create_user_service_graphql
from dto.inputs.sendPhone_input import SendPhoneInput
from dto.inputs.checkCode_input import CheckCodeInput
from dto.inputs.passwordRecoveryWithCedula_input import PasswordRecoveryWithCedulaInput
from dto.inputs.passwordUpdateWithCedula_input import PasswordUpdateWithCedulaInput
from dto.inputs.signup_input import SignUpInput
from dto.types.sendPhoneResponse_type import SendPhoneResponse
from dto.args.status_args import  StatusASrgs
from typing import Any  # Importa el tipo de datos Any
from starlette.requests import Request  # Importa el tipo de datos del objeto Request

# Resto de tu código

 
 
from models.users import UserModels

 

@strawberry.type
class Query:
    

    @strawberry.field(name="findAll", description="Regresa puros []")
    def findAll(self, statusArgs: StatusASrgs = None) -> List[UserModels]:
        data = get_users_GRPHQL_Statusservice(statusArgs)
        objs_list = []  # Inicializa una lista vacía para los objetos modificados 

        for d in data:  # Itera sobre los resultados directamente, sin necesidad de convertir a lista
            print(str(d.get('_id')))
            dependent = get_userbyIdRaw_service(str(d.get('_id')))
            if dependent is not None:  # Verifica si el resultado no es None
                name = dependent['name']
                email = dependent['email']
                lastname = dependent['lastname']
                genderId = dependent['genderId']
                birth = dependent['birth']
                user_data = {
                    'id': d.get('_id'),
                    'phone': d.get('phone'),
                    'lastCode': d.get('lastCode'),
                    'token': d.get('token'),
                    'birth':birth,
                    'ci': d.get('ci'),
                    'city': d.get('city'),
                    'email':email,
                    'genderId': genderId,
                    'lastname': lastname,
                    'name': name,
                    'password': d.get('password'),
                    'state': d.get('state'),
                    'roles': d.get('roles'),
                    'isActive': d.get('isActive'),
                    'status': d.get('status')
                }
                # Elimina las entradas con valor None
                user_data = {k: v for k, v in user_data.items() if v is not None}
                objs_list.append(UserModels(**user_data))  # Inicializa UserModels con argumentos nombrados
            else:
                # Manejar el caso en el que dependent es None
                # Puedes imprimir un mensaje de error o tomar otra acción apropiada
                print(f"Error: No se encontró el usuario para el ID: {d.get('_id')}")

        return objs_list

     
 
#get_adsbyId_GRPHQL_service

@strawberry.type
class Mutation:
    @strawberry.mutation(name="sendPhoneSms", description="Send a sms phone")
    def sendPhoneSms(self, input: SendPhoneInput) -> SendPhoneResponse:
        resul = sendSms_graphql_service(input)
        response = {k: v for k, v in resul.items() if v is not None}
        return SendPhoneResponse(**response)

    @strawberry.mutation(name="checkCode", description="CheckCode sent from a sms phone")
    def checkCode(self, input: CheckCodeInput) -> SendPhoneResponse:
        resul = checkCode_service_graphql(input)
        response = {k: v for k, v in resul.items() if v is not None}
        return SendPhoneResponse(**response)

    @strawberry.mutation(name="signUp", description="signUp user")
    @jwt_required()  # Enforce JWT authentication check
    def signUp(self, input: SignUpInput, info: strawberry.Info) -> SendPhoneResponse:
        # Ensure that the user is authenticated before proceeding
        # Access the user identity from the JWT token if needed
        user_identity = get_jwt_identity()
        #print(user_identity)
        # Assuming create_user_service_graphql returns a dictionary
        resul = create_user_service_graphql(input, info.context['request'])
        response = {k: v for k, v in resul.items() if v is not None}
        # Ensure that the attributes match the ones defined in SendPhoneResponse
        return SendPhoneResponse(**response)

    @strawberry.mutation(name="passwordRecovery", description="Password Recovery")
    def passwordRecovery(self, input: PasswordRecoveryWithCedulaInput) -> SendPhoneResponse:
        #print(user_identity)
        # Assuming create_user_service_graphql returns a dictionary
        resul = check_CI_service_graphql(input)
        response = {k: v for k, v in resul.items() if v is not None}
        # Ensure that the attributes match the ones defined in SendPhoneResponse
        return SendPhoneResponse(**response)

    @strawberry.mutation(name="passwordUpdate", description="Password Update")
    def passwordUpdate(self, input: PasswordUpdateWithCedulaInput) -> SendPhoneResponse:
        #print(user_identity)
        # Assuming create_user_service_graphql returns a dictionary
        resul = check_CI_service_graphql(input)
        response = {k: v for k, v in resul.items() if v is not None}
        # Ensure that the attributes match the ones defined in SendPhoneResponse
        return SendPhoneResponse(**response)


userSchema = strawberry.Schema(query=Query, mutation=Mutation)