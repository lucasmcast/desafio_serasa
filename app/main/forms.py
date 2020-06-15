from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField, SelectField, FileField
from wtforms.validators import DataRequired, StopValidation
from ..models import Empresa
import json

def validate_type_file(form, field):
    file = form.file_upload.data
    type_file = file.content_type

    if not type_file == 'application/json':
        raise StopValidation("Tipo que arquivo invalido")

def validate_data(form, field):
    file = form.file_upload.data
    file.save('tmp/tmp.json')

    with open('tmp/tmp.json', 'r') as json_file:
        dados = json.load(json_file)
    
    empresa = Empresa.query.filter_by(cnpj=dados['cnpj']).first()
    
    if empresa is None:
        raise StopValidation("Empresa não encontrada")

class FormEmpresa(FlaskForm):
    fantasia = TextField('Fantasia', validators=[DataRequired()])
    razao_social = TextField('Razão Social')
    cnpj = TextField('CNPJ', validators=[DataRequired()])
    endereco = TextField('Endereço')
    email = TextField('Email')
    button_cadastrar = SubmitField('Cadastrar')

class FormNotaFiscal(FlaskForm):
    
    empresa = SelectField()
    submit = SubmitField('Emitir Nota Fiscal')

class FormDebito(FlaskForm):
    empresa = SelectField()
    valor_debito = TextField('Valor do Débito')
    submit = SubmitField('Novo Débito')

class FormUploadFile(FlaskForm):
    file_upload = FileField("Escolher Arquivo", validators=[DataRequired(), validate_type_file, validate_data])
    submit = SubmitField('Upload')

    