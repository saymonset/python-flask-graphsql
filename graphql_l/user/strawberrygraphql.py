import strawberry
from typing import List, Optional

import random
from typing import Optional
from services.user import get_users_GRPHQL_Statusservice
from services.ads_graphql_srv import get_adsList_GRPHQLservice, get_adsList_GRPHQL_Statusservice, get_adsbyId_GRPHQL_service, \
delete_ads_GRAPHQL_service, create_ads_GRAPHQL_service, update_ads_GRAPHQL_service, get_totalads_GRPHQLservice, \
get_totalActivosads_GRPHQLservice, get_totalDeletessads_GRPHQLservice
from dto.inputs.create_ads_input import CreateAdsInput
from dto.inputs.update_ads_input import  UpdateAdsInput
from dto.args.status_args import  StatusASrgs
from dto.types.aggregations_type import  AggregationsType
from models.ads import AdsModels
from models.users import UserModels

 

@strawberry.type
class Query:
    

    @strawberry.field(name="findAll", description="Regresa puros []")
    def findAll(self, statusArgs: StatusASrgs = None) -> List[UserModels]:
        data = get_users_GRPHQL_Statusservice(statusArgs)
        objs_list = []  # Inicializa una lista vacía para los objetos modificados 

        for d in data:  # Itera sobre los resultados directamente, sin necesidad de convertir a lista
            user_data = {
                'id': d.get('_id'),
                'phone': d.get('phone'),
                'lastCode': d.get('lastCode'),
                'token': d.get('token'),
                'birth': d.get('birth'),
                'ci': d.get('ci'),
                'city': d.get('city'),
                'email': d.get('email'),
                'genderId': d.get('genderId'),
                'lastname': d.get('lastname'),
                'name': d.get('name'),
                'password': d.get('password'),
                'state': d.get('state'),
                'roles': d.get('roles'),
                'status': d.get('status')
            }
            # Elimina las entradas con valor None
            user_data = {k: v for k, v in user_data.items() if v is not None}
            objs_list.append(UserModels(**user_data))  # Inicializa UserModels con argumentos nombrados

        return objs_list


    @strawberry.field(name="findAllActivos", description="Regresa ads actviods")
    def findActivosAll(self) -> List[AdsModels]:
        statusArgs = StatusASrgs(status=True)
        data = get_adsList_GRPHQL_Statusservice(statusArgs)
        ads_list = []  # Initialize an empty list for the modified objects 
        for d in data:
            id = d['_id']
            title = d['title']
            img = d['img']
            link = d['link']
            status = d['status']
            ads_list.append(AdsModels(id =  id, title=title, img=img, link=link, status=status))  # Initialize AdsModels with named arguments
        return ads_list

    @strawberry.field(name="findAllDelete", description="Regresa ads borrados")
    def findDeleteAll(self) -> List[AdsModels]:
        statusArgs = StatusASrgs(status=False)
        data = get_adsList_GRPHQL_Statusservice(statusArgs)
        ads_list = []  # Initialize an empty list for the modified objects 
        for d in data:
            id = d['_id']
            title = d['title']
            img = d['img']
            link = d['link']
            status = d['status']
            ads_list.append(AdsModels(id =  id, title=title, img=img, link=link, status=status))  # Initialize AdsModels with named arguments
        return ads_list

    @strawberry.field(name="findAggregations", description="Agregations ")
    def findAggregations(self) -> AggregationsType:
        return AggregationsType(
            total = get_totalads_GRPHQLservice(),
            deleteds= get_totalDeletessads_GRPHQLservice(),
            actives = get_totalActivosads_GRPHQLservice()
        )

    @strawberry.field(name="findAllObj", description="Regresa puros []")
    def findAllObj(self) -> List[AdsModels]:
        data = get_adsList_GRPHQLservice(1000, 0)
        ads_list = []  # Initialize an empty list for the modified objects 
        for d in data:
            id = d['_id']
            title = d['title']
            img = d['img']
            link = d['link']
            status = d['status']
            ads_list.append(AdsModels(id =  id, title=title, img=img, link=link, status=status))  # Initialize AdsModels with named arguments
        return ads_list

   

    @strawberry.field(name="findOne", description="Uno solo")
    def findOne(self, id: strawberry.ID) -> AdsModels:
        d = get_adsbyId_GRPHQL_service(id)
        id = d['_id']
        title = d['title']
        img = d['img']
        link = d['link']
        status = d['status']
        return AdsModels(id = id, title=title, img=img, link=link, status=status)
 
#get_adsbyId_GRPHQL_service

@strawberry.type
class Mutation:
    @strawberry.mutation(name="createAds", description="Crea ads")
    def create_AdsModels(self, input: CreateAdsInput) -> AdsModels:
        return create_ads_GRAPHQL_service(input)

    @strawberry.mutation(name="updateAds", description="Update ads")
    def updateAds(self, input: UpdateAdsInput) -> AdsModels:
        return update_ads_GRAPHQL_service(input)

    @strawberry.mutation(name="removeAds", description="Remove ads")
    def remove_AdsModels(self, id: strawberry.ID) -> bool:
        return delete_ads_GRAPHQL_service(id)
 
    
userSchema = strawberry.Schema(query=Query, mutation=Mutation)