try:
  import unzip_requirements
except ImportError:
  pass
import os, jwt
from pymongo import MongoClient
from repository.user import   find_one_repo
from bson import ObjectId
from repository.blacklist import    crear_blacklists_repo, find_one_blacklist_repo
from datetime import datetime, timedelta
from flask_jwt_extended import get_jwt_identity

conn = MongoClient(os.environ.get('MONGO_URI'))
secret = os.environ.get('JWT_SECRET')
db = conn.mic_serv_users

def verifyToken(request):
    """
    The `verifyToken` function checks if a token is valid and not blacklisted, and generates a policy
    document for authorization.
    """
     
   
    token = request.headers.get('Authorization')
     
    if token is None or "Bearer" not in token:
       
        return {'Token': False,'usuario':'unauthorized', 'resp':False,'statusCode':401, 'message': 'unauthorized'}
    try:
      userId = get_jwt_identity()
      if (userId):
        query = {'_id': ObjectId(userId) }
        usuario = find_one_repo(query)
        
        if usuario is not None:
            return {'token': True,  'usuario':usuario, 'resp':True, 'message': 'success'}
        else:
            return {'token': False, 'error':'token no es valido  ', 'resp':False,'statusCode':401, 'message': 'token no es valido'}
      else:
        return {'token': False,'usuario':'unauthorized', 'resp':False, 'statusCode':401, 'message': 'unauthorized'}
    except Exception as e:
            print( e)
            return {'error': 'Invalid token', 'resp':False, 'statusCode':401, 'message': 'Invalid token'}