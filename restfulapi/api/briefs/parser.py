from flask_restplus import reqparse
from pip._vendor.pkg_resources import require

filter_args = reqparse.RequestParser()
filter_args.add_argument('companies', type=str, required=False, location='args', default='', help='Set the list fo companies to be included in the reporte')

headers_args = reqparse.RequestParser()
headers_args.add_argument('XX-AUTH-TOKEN', type=str, required = True, location = 'headers', default= '', help='Set the JWT token generated at first login at /auth/login/ method')
