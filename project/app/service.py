from calendar import timegm
from datetime import datetime,timedelta
import jwt
from rest_framework_jwt.compat import gettext_lazy as _, jwt_version, jwt_decode, ExpiredSignature
from rest_framework_jwt.settings import api_settings
from rest_framework.utils.encoders import JSONEncoder
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_jwt.utils import jwt_create_payload,jwt_encode_payload

#simplified version of generating token
    #instead of writing the functions for token generation, just imported the functions from documentation and used them here.
def jwt_token(user):
    payload=jwt_create_payload(user)
    token=jwt_encode_payload(payload)
    return token
##

def jwt_get_secret_key(payload=None):
    """
    For enhanced security you may want to use a secret key based on user.

    This way you have an option to logout only this user if:
        - token is compromised
        - password is changed
        - etc.
    """

    if api_settings.JWT_GET_USER_SECRET_KEY:
        username = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER(payload)
        User = get_user_model()
        
        # Make sure user exists
        try:
            user = User.objects.get_by_natural_key(username)
        except User.DoesNotExist:
            msg = _("User doesn't exist.")
            raise serializers.ValidationError(msg)
        
        key = api_settings.JWT_GET_USER_SECRET_KEY(user)
        return key
    return api_settings.JWT_SECRET_KEY

#creates payload and generates token
def jwt_generate_token(user):
    #payload
    payload ={
        'email':user.email, 
        'exp':datetime.utcnow()+api_settings.JWT_EXPIRATION_DELTA,
        'iat': datetime.utcnow().timestamp(),
    }
    if api_settings.JWT_AUDIENCE is not None:
        payload['aud'] = api_settings.JWT_AUDIENCE
    if api_settings.JWT_ISSUER is not None:
        payload['iss'] = api_settings.JWT_ISSUER

    #token
    headers=None
    signing_algorithm = api_settings.JWT_ALGORITHM
    if isinstance(signing_algorithm,list):
        signing_algorithm = signing_algorithm[0]
    if signing_algorithm.startswith("HS"):
        key = jwt_get_secret_key(payload)
    else:
        key = api_settings.JWT_PRIVATE_KEY

    if isinstance(key, dict):
        kid, key = next(iter(key.items()))
        headers = {"kid": kid}
    elif isinstance(key,list):
        key = key[0]

    enc = jwt.encode(payload, key, signing_algorithm, headers=headers, json_encoder=JSONEncoder)
    if jwt_version == 1:
        enc = enc.decode()
    return enc