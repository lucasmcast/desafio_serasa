from . import db

class Empresa(db.Model):

    __tablename__ = 'empresas'
    id_empresa = db.Column(db.Integer, primary_key=True)
    fantasia = db.Column(db.String(80))
    razao_social = db.Column(db.String(80))
    cnpj = db.Column(db.String(18), unique=True)
    email = db.Column(db.String(60))
    indice = db.Column(db.Integer)
    notas = db.relationship('NotaFiscal', backref='empresa', lazy='dynamic')
    debitos = db.relationship('Debito', backref='empresa', lazy='dynamic')

    def __repr__(self):
        return f'<Empresa id={self.id_empresa}, fantasia={self.fantasia}\
            razao_social={self.razao_social}, cnpj={self.cnpj}, indice={self.indice}'

    def to_json(self):
        json_generate = {
            'id_empresa' : self.id_empresa,
            'fantasia' : self.fantasia,
            'razao_social' : self.razao_social,
            'cnpj' : self.cnpj,
            'email' : self.email,
            'indice' : self.indice
        }
        return json_generate

class NotaFiscal(db.Model):
    
    __tablename__ = 'notas_fiscais'
    id_nota = db.Column(db.Integer, primary_key=True)
    numero_nota = db.Column(db.String(50), unique=True)
    data_emisao = db.Column(db.String(20))
    id_empresa = db.Column(db.Integer, db.ForeignKey('empresas.id_empresa'))
    itens_nota = db.relationship('NotaFiscalItens', backref='notafiscal', lazy='dynamic')

    def __repr__(self):
        return f'<NotaFiscal id={self.id_nota}, numero_nota={self.numero_nota}\
            , id_empresa={self.id_empresa}'
    
    def to_json(self, empresa):
        json_generate = {
            'numero_nota' : self.numero_nota,
            'empresa' : empresa,
            'data_emisao' : self.data_emisao
        }
        return json_generate
    
    @staticmethod
    def calculo_nota_fiscal(indice=None, perc=None):
        """Função resposavel por somar porcentagem em cima do indece a cada nota emitida"""
        if indice and perc:
            quociente = indice / 100
            result = quociente * perc
            valor_final = indice + result

            if valor_final > 100:
                valor_final = 100
            elif valor_final <= 0:
                valor_final = 1
            
            return int(valor_final)
        else:
            print("Valores para o calculo não foram informados")



class NotaFiscalItens(db.Model):
    
    __tablename__ = 'itens_nota'
    id_nota_itens = db.Column(db.Integer, primary_key=True)
    descricao_prod = db.Column(db.String(50))
    qtd_prod = db.Column(db.Integer)
    numro_nota = db.Column(db.Integer, db.ForeignKey('notas_fiscais.numero_nota'))
    

class ConfCalculo(db.Model):

    __tablename__ = 'conf_calculo'
    id_conf_calc = db.Column(db.Integer, primary_key=True)
    base_nota = db.Column(db.Integer)
    base_debito = db.Column(db.Integer)
    base_indice = db.Column(db.Integer)

class Debito(db.Model):

    __tablename__ = 'debitos'
    id_debito = db.Column(db.Integer, primary_key=True)
    valor_debito = db.Column(db.Integer)
    id_empresa = db.Column(db.Integer, db.ForeignKey('empresas.id_empresa'))
    data_debito = db.Column(db.String(20))

    def __repr__(self):
        return f'<Debito id_debito={self.id_debito}, valor_debito={self.valor_debito},\
            id_empresa={self.id_empresa}, data_debito={self.data_debito}'

    def to_json(self, empresa):
        json_generate = {
            'empresa' : empresa,
            'valor' : self.valor_debito,
            'data_debito' : self.data_debito
        }
        return json_generate
    
    @staticmethod
    def calculo_debito(indice=None, perc=None):
        """Função responsável por fazer o calculo subtraindo o indece pela porcentagem a cada debito realizado"""
        if indice and perc:
            quociente = indice / 100
            result = quociente * perc
            indice -= result

            if quociente < 1:
                resto = round(indice % 1, 2)
                arredondamento = 1 - resto
                indice += arredondamento
            
            if indice > 100:
                indice = 100
            elif indice <= 0:
                indice = 1

            return int(indice)
        else:
            print("Valores para o calculo não foram informados")
