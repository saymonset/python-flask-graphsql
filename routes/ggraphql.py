from flask import Blueprint
from flask_restx import Namespace, Resource, fields, Api
from flask import request, Response, Flask
import json
from bson.objectid import ObjectId
from validators.specialities import isValidSpeciality
from repository.ads  import isValidBdAds, isValidBdAdsUpdate
from services.ggraphql import  get_adsbyId_service 
ns_graphql = Namespace('graphql', 'graphql related endpoints')

model = ns_graphql.model('graphql', {
    'title': fields.String(required=True, description='Name of the graphql'),
    'img': fields.String(required=True, description='Url of the img graphql'),
    'link': fields.String(required=True, description='Link of the graphql'),
})


 

@ns_graphql.route('/', methods = [ 'GET' ])
class get_graphqlList(Resource):        
    def get(self, limite=None, desde=None):
        return get_adsbyId_service()

