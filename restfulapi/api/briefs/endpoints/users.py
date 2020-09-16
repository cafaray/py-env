import logging

from flask import request # , make_response
from flask_restplus import Resource
from api.briefs.services.auth import login
from api.briefs.serializer import user, token, jwt_token
#from api.briefs.parsers import pagination_arguments
from api.commons import api
from models.model import User
from werkzeug.security import check_password_hash, hashlib
import jwt
import datetime
import settings

log = logging.getLogger(__name__)

ns = api.namespace('auth/login', description='Do the login in the app')

@ns.route('/')
class Login(Resource):
    @api.expect(token)
    @api.marshal_with(jwt_token)
    def post(self):
        """
        Do the login to the application. Let the identification and create a jwt token with user info
        """   
        result = dict()        
        result['token']=''
        
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return result, 401
        print('authorization', auth)
        loginUser = auth.username
        phrase = auth.password                
        user = login(loginUser)
        if not user:
            return result, 401
        
        phrase = hashlib.md5(phrase.encode())
        print(phrase.hexdigest(),'==', user.phrase)
        if (user.phrase == phrase.hexdigest()):
            print("Pass verification, preparing token")
            token = jwt.encode({'id': user.idusuari, 'username': user.dsusuari, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, settings.SECRET_KEY)            
            jwtToken = token.decode('UTF-8')
            result['token']=jwtToken
            return result, 201

        print("Pass failed")
        return result, 401