import os
import json
from flask import request, _request_ctx_stack
from functools import wraps
from jose import jwt
from urllib.request import urlopen
from os import abort


AUTH0_DOMAIN = os.environ["AUTH0_DOMAIN"]
ALGORITHMS = os.environ["ALGORITHMS"]
API_AUDIENCE = os.environ["API_AUDIENCE"]


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def get_token_auth_header():
    authO = request.headers.get('Authorization', None)
    # print(authO, "show me the token plz")
    if not authO:
        raise AuthError({
            'code': 'Authorization_header_missing',
            'description': 'Authorization header is expected'
        }, 401)
    auth_p = authO.split()
    # print(auth_p)
    if auth_p[0].lower() != 'bearer':
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization header must be start with "Bearer'
        }, 401)

    elif len(auth_p) == 1:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Token not found'
        }, 401)

    elif len(auth_p) > 2:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization header must be bearer token'
        }, 401)
    token = auth_p[1]
    return token



def check_permissions(permission, payload):
    if'permissions'not in payload:
        raise AuthError({
            'code': 'invalid_claims',
            'description': 'Permissions not included in JWT.'
        }, 403)

    if permission not in payload['permissions']:
        raise AuthError({
            'code': 'unauthorized',
            'description': 'permission not found'
        }, 403)
    return True


def verify_decode_jwt(token):
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    # print(jwks, "list of keys")
    unverified_header = jwt.get_unverified_header(token)
    # print(unverified_header)
    my_key = {}
    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization malformed.'
        }, 401)

    for i in jwks['keys']:
        if i['kid'] == unverified_header['kid']:
            my_key = {
                'kty': i['kty'],
                'kid': i['kid'],
                'use': i['use'],
                'n': i['n'],
                'e': i['e']
            }
        if my_key:
            try:
                payload = jwt.decode(
                    token,
                    my_key,
                    algorithms=ALGORITHMS,
                    audience=API_AUDIENCE,
                    issuer='https://' + AUTH0_DOMAIN + '/')

                return payload

            except jwt.ExpiredSignatureError:
                raise AuthError({
                    'code': 'token_expired',
                    'description': 'Token expired'
                }, 401)

            except jwt.JWTClaimsError:
                raise AuthError({
                    'code': 'invalid_claims',
                    'description': 'Please, check the audience and issuer.'
                }, 401)
            except Exception:
                raise AuthError({
                    'code': 'invalid_header',
                    'description': 'unable to find the appropriate token'
                }, 400)
            raise AuthError({
                'code': 'invalid_header',
                'description': 'unable to find the appropriate key'
            })


# raise Exception('Not Implemented')


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()

            payload = verify_decode_jwt(token)

            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator
