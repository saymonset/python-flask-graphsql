from flask import Blueprint
from flask_restx import Namespace, Resource, fields, Api
from flask import request, Response, Flask
import json
from bson.objectid import ObjectId
from validators.specialities import isValidSpeciality
from repository.planVaccineDependent  import isValidBdplanVaccineDependent, isValidBdplanVaccineDependentUpdate
from services.planVaccineDependent import delete_planVaccineDep_service, create_planVaccineDependent_service, get_planVaccineDependentList_service
from services.planVaccineDependent import get_planVaccineDependentBYIDservice

ns_planVaccineDependent = Namespace('planVaccineDependent', 'planVaccineDependent related endpoints')

model = ns_planVaccineDependent.model('planVaccineDependent', {
    'dependent_id': fields.String(required=True, description='dependent_id missing planVaccineDependent'),
    'vacinne_id': fields.String(required=True, description='vacinne_id missing of planVaccineDependent'),
})


@ns_planVaccineDependent.route('/', methods = [ 'POST' ])
class getplanVaccineDependentsswgger(Resource):
    @ns_planVaccineDependent.expect(model, validate=True)
    def post(self,  **kwargs):
       # Obtener los datos del objeto enviado en la solicitud
        data = ns_planVaccineDependent.payload
        
        return create_planVaccineDependent_service(data) 

@ns_planVaccineDependent.route('/<limite>/<desde>', methods = [ 'GET' ])
class get_planVaccineDependentList(Resource):        
    @ns_planVaccineDependent.doc(params={'limite': {'default': 20}, 'desde': {'default': 0}})
    def get(self, limite=None, desde=None):
        return get_planVaccineDependentList_service(limite, desde)


@ns_planVaccineDependent.route('/<id>', methods = [  'GET', 'PUT', 'DELETE' ])
class getplanVaccineDependentswgger(Resource):
    def get(self, id):
        return get_planVaccineDependentBYIDservice(id)
        #return get_planvaccinedependentbyId_service(id)
    def delete(self, id):
        return delete_planVaccineDep_service(id)     
    



 

