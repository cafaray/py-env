import logging.config
import os
from flask import Flask, Blueprint
import settings
from api.briefs.endpoints.users import ns as ns_user
from api.briefs.endpoints.companies import ns as ns_company
from api.commons import api
from models.model import db

app = Flask(__name__)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)

def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
    flask_app.config['SECRET_KEY'] = settings.SECRET_KEY


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(ns_user)
    api.add_namespace(ns_company)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)

def main():
    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG)


if __name__ == "__main__":
    main()

#api = Api(app, version='1.0', title='TodoMVC API',
#    description='A simple TodoMVC API',
#)

# services
# ns = api.namespace('todos', description='TODO operations')

# models.model_todo.py:
#todo = api.model('Todo', {
#    'id': fields.Integer(readOnly=True, description='The task unique identifier'),
#    'task': fields.String(required=True, description='The task details')
#})

# repository.repo_todo.py
#class TodoDAO(object):
#    def __init__(self):
#        self.counter = 0
#        self.todos = []
#
#    def get(self, id):
#        for todo in self.todos:
#            if todo['id'] == id:
#                return todo
#        api.abort(404, "Todo {} doesn't exist".format(id))
#
#    def create(self, data):
#        todo = data
#        todo['id'] = self.counter = self.counter + 1
#        self.todos.append(todo)
#        return todo
#   def update(self, id, data):
#        todo = self.get(id)
#        todo.update(data)
#        return todo
#
#    def delete(self, id):
#        todo = self.get(id)
#        self.todos.remove(todo)


#@ns.route('/')
#class TodoList(Resource):
#    '''Shows a list of all todos, and lets you POST to add new tasks'''
#    @ns.doc('list_todos')
#    @ns.marshal_list_with(todo)
#    def get(self):
#        '''List all tasks'''
#        return DAO.todos

#    @ns.doc('create_todo')
#    @ns.expect(todo)
#    @ns.marshal_with(todo, code=201)
#    def post(self):
#        '''Create a new task'''
#        return DAO.create(api.payload), 201


#@ns.route('/<int:id>')
#@ns.response(404, 'Todo not found')
#@ns.param('id', 'The task identifier')
#class Todo(Resource):
#    '''Show a single todo item and lets you delete them'''
#    @ns.doc('get_todo')
#    @ns.marshal_with(todo)
#    def get(self, id):
#        '''Fetch a given resource'''
#        return DAO.get(id)

#    @ns.doc('delete_todo')
#    @ns.response(204, 'Todo deleted')
#    def delete(self, id):
#        '''Delete a task given its identifier'''
#        DAO.delete(id)
#        return '', 204

#    @ns.expect(todo)
#    @ns.marshal_with(todo)
#    def put(self, id):
#        '''Update a task given its identifier'''
#        return DAO.update(id, api.payload)

def main():
    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG)

if __name__ == '__main__':
    # app.run(debug=True)
    main()
