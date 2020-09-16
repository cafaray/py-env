import logging
import traceback
from functools import wraps
from flask import request
from flask_restplus import Api
import settings
import jwt
from sqlalchemy.orm.exc import NoResultFound 
log = logging.getLogger(__name__)

api = Api(version='1.0', title='My Blog API',
          description='A simple demonstration of a Flask RestPlus powered API')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'XX-AUTH-TOKEN' in request.headers:
            token = request.headers['XX-AUTH-TOKEN']
        if not token:
            return {'message': 'Token is missing'}, 401
        try:
            data = jwt.decode(token, settings.SECRET_KEY)
            id_user = data['id']
            print('token.user:', data['id'])
        except:
            return {'message': 'Token is not valid'}, 401
        return f(id_user, *args, **kwargs)
    return decorated

@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {'message': 'A database result was required but none was found.'}, 404
