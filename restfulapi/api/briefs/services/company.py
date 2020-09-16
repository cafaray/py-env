from models import db
from models.model import Company

def companies(data):
    iduser = data.get('iduser')
    return Company.query.filter(Company.idusuari == iduser).get_or_404(description='There is no companies associated to {}'.format(iduser))
