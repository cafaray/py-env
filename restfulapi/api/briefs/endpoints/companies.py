import logging

from flask import request
from flask_restplus import Resource
from api.briefs.services.company import companies
from api.briefs.serializer import company, filterin
from api.briefs.parser import filter_args, headers_args
from api.commons import api
from models.model import Company
from api.commons import token_required

log = logging.getLogger(__name__)

ns = api.namespace('briefs', description='Retrieve all the companies associated to the user logged')

@ns.route('/')
class Company(Resource):
    @token_required
    @api.expect(filter_args, headers_args)
    @api.marshal_with(company)
    def get(idUser,data):
        """
        Do the login to the application. Let the identification and create a jwt token with user info
        """
        print('jwt:', request.headers['XX-AUTH-TOKEN'])
        print(request.json)                
        return None, 200