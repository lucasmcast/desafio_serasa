from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField, SelectField, FileField
from wtforms.validators import DataRequired, StopValidation
from ..models import Empresa, NotaFiscal, Debito
from .. import db
import json

def validate_nota(dados):
    for nota in dados['notas']:
        nota_db = NotaFiscal.query.filter_by(numero_nota=nota['numero_nota']).first()
        if nota_db:
            raise StopValidation("Arquivo contém nota fiscal já cadastrada")
    

def validate_empresa(form, field):
    cnpj = form.cnpj.data

    empresa = Empresa.query.filter_by(cnpj=cnpj).first()

    if empresa:
        raise StopValidation("Empresa já Cadastrada")

def validate_type_file(form, field):
    file = form.file_upload.data
    type_file = file.content_type

    if not type_file == 'application/json':
        raise StopValidation("Tipo que arquivo inválido")

def validate_data(form, field):
    notas = []
    debitos = []
    index = int(form.empresa.data)
    
    empresa_selected = form.empresa.choices[index][1]
    empresa = Empresa.query.filter_by(cnpj=empresa_selected[1]).first()
    indice = empresa.indice

    file = form.file_upload.data
    file.save('tmp/tmp.json')

    with open('tmp/tmp.json', 'r') as json_file:
        dados = json.load(json_file)

    validate_nota(dados)

    try:
        dados['cnpj']
    except:
        raise StopValidation('Arquivo com chave CNPJ invalido')

    if empresa_selected[1] != dados['cnpj']:
        raise StopValidation("CNPJ das Empresas não conferem")
    
    #Executando o calculo do indice, das notas recebidas pelo aquivo json
    indice = calculo_nota_fiscal(notas, dados, empresa, indice)

    #Executando o calculo do indice, dos debitos recebidos pelo aquivo json
    indice = calculo_debito(debitos, dados, empresa, indice)

    empresa.indice = indice

    db.session.add_all(notas)
    db.session.add_all(debitos)
    db.session.add(empresa)
    db.session.commit()



def calculo_nota_fiscal(notas, dados_json, empresa, indice):
    """Faz o calculo das notas, conforme dados recebitos pelo arquivo json"""
    try:
        for nota in dados_json['notas']:
            notas.append(
                NotaFiscal(
                    numero_nota=nota['numero_nota'],
                    data_emisao=nota['data_emissao'],
                    empresa=empresa
                )
            )
            indice = NotaFiscal.calculo_nota_fiscal(indice, 2)

        return indice
    except:
        raise StopValidation("Arquivo contém chave inválida. {notas, numero_nota ou data_emisao}")

def calculo_debito(debitos, dados_json, empresa, indice):
    """Faz o calculo dos debitos, conforme dados recebitos pelo arquivo json"""
    try:
        for debito in dados_json['debitos']:
            debitos.append(
                Debito(
                    data_debito=debito['data_debito'],
                    empresa=empresa
                )
            )
            indice = Debito.calculo_debito(indice, 4)

        return indice
    except:
        raise StopValidation("Arquivo contém chave inválida. {debitos, data_debito ou valor_debito}")


class FormEmpresa(FlaskForm):
    fantasia = TextField('Fantasia', validators=[DataRequired()])
    razao_social = TextField('Razão Social')
    cnpj = TextField('CNPJ', validators=[DataRequired(), validate_empresa])
    button_cadastrar = SubmitField('Cadastrar')

class FormNotaFiscal(FlaskForm):
    
    empresa = SelectField(validators=[DataRequired()])
    submit = SubmitField('Emitir Nota Fiscal')

class FormDebito(FlaskForm):
    empresa = SelectField(validators=[DataRequired()])
    submit = SubmitField('Novo Débito')

class FormUploadFile(FlaskForm):
    file_upload = FileField("Escolher Arquivo", validators=[DataRequired(), validate_type_file, validate_data])
    empresa = SelectField("Fantasia, CNPJ", validators=[DataRequired()])
    submit = SubmitField('Upload')

    