from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField, SelectField
from wtforms.validators import DataRequired

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