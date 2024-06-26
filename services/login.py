from bson import json_util
import json
from repository.user import    validateUser, validateUserByEmail, get_user_repo
from repository.dependent import    checkUserDependent
from flask_jwt_extended import create_access_token
from dto.inputs.loginI_input import LoginInput

"""Login de objetos"""


def loginGraphql(udata:LoginInput):
    isVal, id, user = validateUser(udata.ci, udata.password)
    if isVal:
        token = create_access_token(identity=str(user["_id"]), expires_delta=False)
        dependent_is_user = checkUserDependent({"isUser": True, "user_id": str(id)})
        user = json_util.dumps(user)
        dependent_is_user = json_util.dumps(dependent_is_user)
        response = {
            "statusCode": 200,
            "token": token,
            "usuario": json.loads(user),
            "more": json.loads(dependent_is_user),
            "resp":True,
            "message":"successful"
        }
        return response
    response = {"statusCode": 401, "message": "Unauthorized", "resp":False}
    return response

def login(udata):
    isVal, id, user = validateUser(udata['ci'], udata['password'])
    if isVal:
        token = create_access_token(identity=str(user["_id"]), expires_delta=False)
        dependent_is_user = checkUserDependent({"isUser": True, "user_id": str(id)})
        user = json_util.dumps(user)
        dependent_is_user = json_util.dumps(dependent_is_user)
        response = {
            "statusCode": 200,
            "token": token,
            "usuario": json.loads(user),
            "more": json.loads(dependent_is_user),
            "resp":True,
            "message":"successful"
        }
        return response
    response = {"statusCode": 401, "message": "Unauthorized", "resp":False}
    return response

def checkStatus(id):
    user = get_user_repo(id)
    if user:  # Check if user is valid or has data
        token = create_access_token(identity=str(id), expires_delta=False)
        dependent_is_user = checkUserDependent({"isUser": True, "user_id": user['_id']})
        print(user)
        user = json_util.dumps(user)
        dependent_is_user = json_util.dumps(dependent_is_user)
        response = {
            "statusCode": 200,
            "token": token,
            "usuario": json.loads(user),
            "more": json.loads(dependent_is_user),
            "resp":True,
            "message":"successful"
        }
        return response
    response = {"statusCode": 401, "message": "Unauthorized", "resp":False}
    return response    

"""Login de objetos"""

def loginByMail(udata):
    isVal, id, user = validateUserByEmail(udata['email'], udata['password'])
    if isVal:
        token = create_access_token(identity=str(user["_id"]), expires_delta=False)
        dependent_is_user = checkUserDependent({"isUser": True, "user_id": id})
        user = json_util.dumps(user)
        dependent_is_user = json_util.dumps(dependent_is_user)
        response = {
            "statusCode": 200,
            "token": token,
            "usuario": json.loads(user),
            "more": json.loads(dependent_is_user),
        }
        return response
    response = {"statusCode": 401, "body": json.dumps({"message": f"Unauthorized"})}
    return response
    