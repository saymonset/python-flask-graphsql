
from flask import Blueprint
from flask_restx import Namespace, Resource, fields, Api
from flask import request, Response, Flask
from services.login import login, loginByMail, checkStatus
from helps.token import verifyToken
from validators.genders import isValidGenders
import json
from bson.objectid import ObjectId
from flask_jwt_extended import jwt_required, JWTManager

 

ns_login = Namespace('login', 'Login related endpoints')
 

login_model = ns_login.model('login', {
    'ci': fields.String(required=False, description='CI of user'),
    'email': fields.String(required=False, description='Email of user'),
    'password': fields.String(required=True, description='Password of user') 
})
 

@ns_login.route('/', methods = [ 'POST' ])
class getloginwgger(Resource):
    @ns_login.expect(login_model, validate=True)
    def post(self,  **kwargs):
        # Obtener los datos del objeto enviado en la solicitud
        user_data = ns_login.payload
        return login(user_data) 

@ns_login.route('/mail', methods = [ 'POST' ])
class getloginMailwgger(Resource):
    @ns_login.expect(login_model, validate=True)
    def post(self,  **kwargs):
        # Obtener los datos del objeto enviado en la solicitud
        user_data = ns_login.payload
        return loginByMail(user_data) 


@ns_login.route('/checkStatus/<idUser>', methods = [ 'GET' ])
class getcheckstatuswgger(Resource):       
   @ns_login.doc(security='apikey')
   @jwt_required() 
   def get(self, idUser):
      return checkStatus(idUser)

 