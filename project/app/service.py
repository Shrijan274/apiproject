from calendar import timegm
from datetime import datetime
import jwt
from rest_framework_jwt.compat import gettext_lazy as _, jwt_version, jwt_decode, ExpiredSignature
from rest_framework_jwt.settings import api_settings

def jwt_create_payload(user):
    #print(8,user.email)
    #print(api_settings.__dict__)
    payload ={
        'email':user.email, 
        'username':user.username,
        'exp':datetime.utcnow()+api_settings.JWT_EXPIRATION_DELTA
    }
    if api_settings.JWT_ALLOW_REFRESH:
        payload['orig_iat'] = timegm(datetime.utcnow().utctimetuple())
    if api_settings.JWT_AUDIENCE is not None:
        payload['aud'] = api_settings.JWT_AUDIENCE
    if api_settings.JWT_ISSUER is not None:
        payload['iss'] = api_settings.JWT_ISSUER
    #print(21,payload)
    return payload

# def jwt_generate_token():
#     token=jwt.encode(jwt_create_payload(),key,algorithm='HS256')
#     return token


def jwt_generate_token(user):
    payload ={
        'email':user.email, 
        'username':user.username,
        'exp':datetime.utcnow()+api_settings.JWT_EXPIRATION_DELTA
    }
    if api_settings.JWT_ALLOW_REFRESH:
        payload['orig_iat'] = timegm(datetime.utcnow().utctimetuple())
    if api_settings.JWT_AUDIENCE is not None:
        payload['aud'] = api_settings.JWT_AUDIENCE
    if api_settings.JWT_ISSUER is not None:
        payload['iss'] = api_settings.JWT_ISSUER
    key='qwerty123QWERTY!@#'
    token=jwt.encode(payload,key,algorithm='HS256')
    return token
