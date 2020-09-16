from datetime import datetime
from models import db

class Policy(db.Model):
    __tablename__ = 'kusm01t'
    idprofil = db.Column(db.String, primary_key=True)
    dsprofil = db.Column(db.String)
    dspolicy = db.Column(db.String)
    dtfecalt = db.Column(db.DateTime)
    dtfecbaj = db.Column(db.DateTime)
    instatus = db.Column(db.String)

    def __init__(self, profile, policy, alta, baja, estatus='A'):
        self.dsprofil = profile
        self.dspolicy = policy
        self.dtfecalt = alta
        self.dtfecbaj = baja
        self.instatus = estatus
    def __repr__(self):
        return '[Policy %r]' % self.dsprofil

class User(db.Model):
    __tablename__ = 'kusm00t'
    idusuari = db.Column(db.String, primary_key=True)
    dsusuari = db.Column(db.String)
    dsname = db.Column(db.String)
    dsapepat = db.Column(db.String)
    dsapemat = db.Column(db.String)
    dssecnam = db.Column(db.String)
    phrase = db.Column(db.String)
    dtfecalt = db.Column(db.DateTime)
    dtfecbaj = db.Column(db.DateTime)
    instatus = db.Column(db.String)
    nuempres = db.Column(db.Integer)
    iduserpf = db.Column(db.String, db.ForeignKey('kusm01t.idprofil'))

    policy = db.relationship('Policy', foreign_keys=[iduserpf], backref=db.backref('policy', lazy='dynamic'))

    def __init__(self, username, nombre, paterno, materno, secname, phrase, alta, baja, estatus, empresas=None):
        self.dsusuari = username
        self.dsname = nombre
        self.dsapepat = paterno
        self.dsapemat = materno
        self.dssecname = secname
        self.phrase = phrase
        self.dtfecalt = alta
        self.dtfecbaj = baja
        self.instatus = estatus
        if empresas is None:
            empresas = 0
        self.nuempres = empresas
    def __repr__(self):
        return '<User %r>' % self.dsusuari

class Company(db.Model):
    __tablename__ = 'kusm10t'
    idempres = db.Column(db.String, primary_key=True)
    cdempres = db.Column(db.String)
    dsempres = db.Column(db.String)
    dsrfc = db.Column(db.String)
    dslogo = db.Column(db.String)
    dtfecini = db.Column(db.DateTime)
    nuusuari = db.Column(db.Integer)
    dtfecalt = db.Column(db.DateTime)
    dtfecbaj = db.Column(db.DateTime)
    instatus = db.Column(db.String)
    idusuari = db.Column(db.String, db.ForeignKey('kusm00t.idusuari'))
    
    company_user = db.relationship('User', foreign_keys=[idusuari], backref=db.backref('user', lazy='dynamic'))

    def __init__(self, codigo, empresa, rfc, logo, fecha, usuarios, alta, baja, estatus, id_usuario):
        self.cdempres = codigo
        self.dsempres = empresa
        self.dsrfc = rfc
        self.dslogo = logo
        self.dtfecini = fecha
        self.nuusuari = usuarios
        self.dtfecalt = alta
        self.dtfecbaj = baja
        self.instatus = estatus
        self.idusuari = id_usuario

    def __repr__(self):
        return '<Company %r>' % self.dsempres

class Document(db.Model):
    __tablename__ = 'kdem10t'
    iddocele = db.Column(db.String, primary_key=True)
    cddocele = db.Column(db.String)
    dtfecapl = db.Column(db.DateTime)
    iningegr = db.Column(db.String)
    dbimport = db.Column(db.Float)
    intipdoc = db.Column(db.String)
    dtfecalt = db.Column(db.DateTime)
    dtfecbaj = db.Column(db.DateTime)
    idempres = db.Column(db.String, db.ForeignKey('kusm10t.idempres'))
    
    document_company = db.relationship('Company', foreign_keys=[idempres], backref=db.backref('companies', lazy='dynamic'))

    def __init__(self, codigo, fecha, tipo, importe, tipoDocumento, alta, baja, id_empresa):
        self.cddocele = codigo
        self.dtfecapl = fecha
        self.iningegr = tipo
        self.dbimport = importe
        self.intipdoc = tipoDocumento
        self.dtfecalt = alta
        self.dtfecbaj = baja
        self.idempres = id_empresa

    def __repr__(self):
        return '<Document %r>' % self.dbimport