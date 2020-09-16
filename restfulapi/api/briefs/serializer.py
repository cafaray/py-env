from flask_restplus import fields
from api.commons import api

user = api.model('User', {
    'id': fields.String(attribute='idusuari', readOnly=True, description='The unique identifier of a user'),
    'username': fields.String(attribute='dsusuari', required=True, description='Username identified by the source system'),
    'name':   fields.String(attribute='dsname', required=True, description='User first name'),
    'lastname': fields.String(attribute=lambda x: x.dsapepat+' '+x.dsapemat, required=True, description='User lastname'),    
    'secname': fields.String(attribute='dssecnam', required=False, description='Secname'),    
    'companies': fields.Integer(attribute='nuempres', required=True, description='Number of companies linked to the user'),
    'status': fields.String(attribute='instatus', required=True, description='Indicates the state of the company, active/inactive'),
    'policy': fields.String(required=True, description='Policy linked to the user')
})

token = api.model('Token', {
    'username': fields.String(required=True, description='Username identified by the source system'),
    'phrase':   fields.String(required=True, description='Phrase to insure the identified user in the source system'),
})

jwt_token = api.model('JWT-Token', {
    'token': fields.String(required=True, description='Token to identify user logged on'),    
    #'uri': fields.Url(required=False, absolute=True, description='URI to get token'),    
    #'startedAt': fields.DateTime(required=False, description='Created date for the jwt-token')
})

filterin = api.model('Filter-Companies', {
    'companies': fields.String(required=False, description='Set the companies to list separated by semicolon. Ex. 1;2;4')
})

document = api.model('Document', {
    'id': fields.String(attribute='iddocele', readOnly=True, description='The unique identifier of a document'),
    'code': fields.String(attribute='cddocele', required=True, description='Category code, unique identifier for the document from the source system'),
    'dateApply': fields.DateTime(attribute='dtfecapl', required=True, description='The active date of the document in the source system'),
    'direction': fields.String(attribute=lambda x: 'Ingress' if x.iningegr=='I' else 'Egress', required=True, description='Ingress or egress transaction document'),
    'ammount': fields.Float(attribute='dbimport', required=True, description='Amount transaction document'),
    'doctype': fields.String(attribute='intipdoc', required=True, description='Document type to identify the source of the document. C -> Buys, V-> Sales, N-> Salary, I-> Taxes, G-> Expenses, Other one-> Non profit taxes'),    
})

company = api.model('Company', {
    'id': fields.String(attribute='idempres', readOnly=True, description='The unique identifier of a company'),
    'code': fields.String(attribute='cdempres', required=True, description='Company code for identify in the source system'),
    'company': fields.String(attribute='dsempres', required=True, description='Company name'),
    'rfc':    fields.String(attribute='dsrfc', required=True, description='Goverment identifier'),
    'companyLogo':   fields.String(attribute='dslogo', required=False, description='URI Location for the image in the resources folder'),
    'since': fields.DateTime(attribute='dtfecini', required=True, description='The active date of the company in the source system'),
    'users': fields.Integer(attribute='nuusuari', required=True, description='Number of users linked to the company'),
    'status': fields.String(attribute='instatus', required=True, description='Indicates the state of the company, active/inactive'),
    'documents': fields.List(fields.Nested(document))
})

