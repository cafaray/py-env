from models import db
from models.model import User

def login(data):
    username = data
    return User.query.filter(User.dsusuari == username).first_or_404(description='There is no data with {}'.format(username))
