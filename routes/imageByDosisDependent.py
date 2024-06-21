from flask import Blueprint
from flask_restx import Namespace, Resource, fields, Api
from flask import request, Response, Flask
import json
from bson.objectid import ObjectId
from validators.specialities import isValidSpeciality
from services.imageByDosisDependent import delete_imageByDosisDependent_service, create_imageByDosisDependent_service
from services.imageByDosisDependent import get_imageByDosisDependentBYIDservice

ns_imageByDosisDependent = Namespace('imageByDosisDependent', 'imageByDosisDependent related endpoints')

model = ns_imageByDosisDependent.model('imageByDosisDependent', {
    'dependent_id': fields.String(required=True, description='dependent_id missing imageByDosisDependent'),
    'dosis_id': fields.String(required=True, description='dosis_id missing of imageByDosisDependent'),
})


@ns_imageByDosisDependent.route('/', methods = [ 'POST' ])
class getimageByDosisDependentsswgger(Resource):
    @ns_imageByDosisDependent.expect(model, validate=True)
    def post(self,  **kwargs):
       # Obtener los datos del objeto enviado en la solicitud
        data = ns_imageByDosisDependent.payload
        
        return create_imageByDosisDependent_service(data) 



#@ns_dependents.route('/<limite>/<desde>/<id_user>/<query>', methods = [ 'GET' ])
@ns_imageByDosisDependent.route('/<dependent_id>/<dosis_id>', methods = [  'GET',  'DELETE' ])
class getimageByDosisDependentswgger(Resource):
    def get(self, dependent_id, dosis_id):
        return get_imageByDosisDependentBYIDservice(dependent_id, dosis_id)
        #return get_imagebydosisdependentbyId_service(id)
    def delete(self, dependent_id, dosis_id):
        return delete_imageByDosisDependent_service(dependent_id, dosis_id)     
    



 

