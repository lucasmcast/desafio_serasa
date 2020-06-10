from . import db

class Empresa(db.Model):

    __tablename__ = 'empresas'
    id_empresa = db.Column(db.Integer, primary_key=True)
    fantasia = db.Column(db.String(80))
    razao_social = db.Column(db.String(80))
    cnpj = db.Column(db.String(18), unique=True)
    email = db.Column(db.String(60))
    notas = db.relationship('NotaFiscal', backref='empresa', lazy='dynamic')

    def __repr__(self):
        return f'<Empresa id={self.id_empresa}, fantasia={self.fantasia}\
            razao_social={self.razao_social}, cnpj={self.cnpj}'

class NotaFiscal(db.Model):
    
    __tablename__ = 'notas_fiscais'
    id_nota = db.Column(db.Integer, primary_key=True)
    numero_nota = db.Column(db.String, unique=True)
    id_empresa = db.Column(db.Integer, db.ForeignKey('empresas.id_empresa'))

class NotaFiscalItens(db.Model):
    
    __tablename__ = 'itens_nota'
    id_nota_itens = db.Column(db.Integer, primary_key=True)
    descricao_prod = db.Column(db.String(50))
    qtd_prod = db.Column(db.Integer)
    id_nota_fiscal = db.Column(db.Integer, db.ForeignKey('notas_fiscais.id_nota'))
    

class ConfCalculo(db.Model):

    __tablename__ = 'conf_calculo'
    id_conf_calc = db.Column(db.Integer, primary_key=True)
    base_nota = db.Column(db.Integer)
    base_debito = db.Column(db.Integer)
    base_indice = db.Column(db.Integer)

class Debito(db.Model):

    __tablename__ = 'debitos'