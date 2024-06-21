from flask import Blueprint
from flask_restx import Namespace, Resource, fields, Api
from flask import request, Response, Flask
import json
from bson.objectid import ObjectId
from validators.specialities import isValidSpeciality
from repository.schemaVaccineDosisDependents  import isValidBdplanVaccineDependent, isValidBdschemaVaccineDosisDependentsUpdate
from services.schemaVaccineDosisDependents import delete_planVaccineDep_service, create_schemaVaccineDosisDependents_service, get_schemaVaccineDosisDependentsList_service
from services.schemaVaccineDosisDependents import get_schemaVaccineIdDosisIdDependentsservice, get_schemaVaccineDosisDependentBYIDservice, update_schemaVaccineDosisDependent_service, get_schemaVaccineDosisDependentsLoad_service

ns_schemaVaccineDosisDependents = Namespace('schemaVaccineDosisDependents', 'schemaVaccineDosisDependents related endpoints')

model = ns_schemaVaccineDosisDependents.model('schemaVaccineDosisDependents', {
    'dependent_id': fields.String(required=True, description='dependent_id missing schemaVaccineDosisDependents'),
    'dosis_id': fields.String(required=True, description='dosis_id missing schemaVaccineDosisDependents'),
    'vacinne_id': fields.String(required=True, description='vacinne_id missing of schemaVaccineDosisDependents'),
    'expires_in_days': fields.Integer(required=True, description='expires_in_days missing of schemaVaccineDosisDependents'),
    'date_must_apply': fields.String(required=True, description='date_must_apply missing of schemaVaccineDosisDependents'),
    'isApplied': fields.Boolean(required=True, description='isApplied missing of schemaVaccineDosisDependents'),
    'status': fields.Boolean(required=True, description='status missing of schemaVaccineDosisDependents'),
});


@ns_schemaVaccineDosisDependents.route('/', methods = [ 'POST' ])
class getschemaVaccineDosisDependentssswgger(Resource):
    @ns_schemaVaccineDosisDependents.expect(model, validate=True)
    def post(self,  **kwargs):
       # Obtener los datos del objeto enviado en la solicitud
        data = ns_schemaVaccineDosisDependents.payload
        
        return create_schemaVaccineDosisDependents_service(data) 

@ns_schemaVaccineDosisDependents.route('/<limite>/<desde>', methods = [ 'GET' ])
class get_schemaVaccineDosisDependentsList(Resource):        
    @ns_schemaVaccineDosisDependents.doc(params={'limite': {'default': 20}, 'desde': {'default': 0}})
    def get(self, limite=None, desde=None):
        return get_schemaVaccineDosisDependentsList_service(limite, desde)

@ns_schemaVaccineDosisDependents.route('/findDosis_idIdDependent/<dosis_id>/<idDependent>', methods = [ 'GET' ])
class get_schemaVaccineFINDIdDosisIdDependents(Resource):        
    @ns_schemaVaccineDosisDependents.doc(params={'dosis_id': {'default': ''}, 'idDependent': {'default': ''}})
    def get(self, dosis_id=None, idDependent=None):
        return get_schemaVaccineIdDosisIdDependentsservice(dosis_id, idDependent)
        #return "Respuesta de ejemplo"

@ns_schemaVaccineDosisDependents.route('/load', methods = [ 'GET' ])
class get_schemaVaccineDosisDependentsLoad(Resource):        
    def get(self,  **kwargs):
        return get_schemaVaccineDosisDependentsLoad_service()


@ns_schemaVaccineDosisDependents.route('/<id>', methods = [  'GET', 'PUT', 'DELETE' ])
class getschemaVaccineDosisDependentsswgger(Resource):
    def get(self, id):
        return get_schemaVaccineDosisDependentBYIDservice(id)
        #return get_planvaccinedependentbyId_service(id)
    def delete(self, id):
        return delete_planVaccineDep_service(id)   
    @ns_schemaVaccineDosisDependents.expect(model, validate=True)
    def put(self,  id):
       # Obtener los datos del objeto enviado en la solicitud
        data = ns_schemaVaccineDosisDependents.payload
         # Validar campos en BD
        result =  isValidBdschemaVaccineDosisDependentsUpdate(id, data)
        return update_schemaVaccineDosisDependent_service(id, data) if bool(result["resp"])  else result   
    



 

