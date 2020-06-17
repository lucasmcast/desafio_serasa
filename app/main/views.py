from flask import Flask, render_template, redirect, url_for, flash
from datetime import date
from . import main
from .forms import FormEmpresa, FormNotaFiscal, FormDebito, FormUploadFile
from .. import db
from ..models import Empresa, NotaFiscal, Debito, ConfCalculo
import json
import random

@main.route('/', methods=['GET', 'POST'])
def index():
    #ordena a lista de empresa do maior para o menor indice
    empresas = Empresa.query.all()

    empresas_json = [empresa.to_json() for empresa in empresas]
    
    for emp in empresas_json:
        id_empresa = int(emp['id_empresa'])
        notas = NotaFiscal.query.filter_by(id_empresa=id_empresa).all()
        debitos = Debito.query.filter_by(id_empresa=id_empresa).all()
        emp['qtd_notas'] = len(notas)
        emp['qtd_debitos'] = len(debitos)

    empresas_json = sorted(empresas_json, key=lambda k: k['indice'], reverse=True)

    return render_template('index.html', empresas=empresas_json)
    
@main.route('/cadastro', methods=['GET','POST'])
def cadastro():
    # Carrega a base dos calculos
    conf = ConfCalculo.getInstance().getConfCalculo()

    form = FormEmpresa()
    form_upload = FormUploadFile()
    empresas = get_empresas()

    form_upload.empresa.choices = [(str(i), (empresa['fantasia'],empresa['cnpj'])) for i, empresa in enumerate(empresas)]
    if form.validate_on_submit():
        empresa = Empresa(
            fantasia=form.fantasia.data,
            razao_social=form.razao_social.data,
            cnpj=form.cnpj.data,
            indice=conf['base_indice']
        )
        db.session.add(empresa)
        db.session.commit()

        form.fantasia.data = ''
        form.razao_social.data = ''
        form.cnpj.data = ''

        flash("Cadastrado com sucesso")
        empresas = get_empresas()
        form_upload.empresa.choices = [(str(i), (empresa['fantasia'],empresa['cnpj'])) for i, empresa in enumerate(empresas)]

        return render_template('cadastro_empresa.html', form=form, form_upload=form_upload, empresas=empresas)
    
    if form_upload.validate_on_submit():             
        flash("Importado com sucesso")
        return render_template('cadastro_empresa.html', form=form, form_upload=form_upload, empresas=empresas)
    
    return render_template('cadastro_empresa.html', form=form, form_upload=form_upload, empresas=empresas)

@main.route('/notaFiscal', methods=['GET', 'POST'])
def nota_fiscal():
    # Carrega a base dos calculos
    conf = ConfCalculo.getInstance().getConfCalculo()

    form = FormNotaFiscal()
    empresas = get_empresas()
    notas = get_notas()
    form.empresa.choices = [(str(i), (empresa['fantasia'], empresa['cnpj'])) for i, empresa in enumerate(empresas)]

    if form.validate_on_submit():
        index = int(form.empresa.data)
        numero_nota = random.randint(1, 123456)
        empresa = form.empresa.choices[index][1]
        result = Empresa.query.filter_by(cnpj=empresa[1]).first()
        
        nota = NotaFiscal(
            numero_nota=numero_nota,
            data_emisao=date.today(),
            empresa=result
        )
        indice = result.indice
        valor_final = NotaFiscal.calculo_nota_fiscal(indice, conf['base_nota'])
        result.indice = valor_final

        db.session.add(result)
        db.session.add(nota)
        db.session.commit()

        form.empresa.data = ''
        notas = get_notas()

        return render_template('nota_fiscal.html', form=form, notas=notas)

    return render_template('nota_fiscal.html', form=form, notas=notas)

@main.route('/debitos', methods=['GET', 'POST'])
def debito():
    # Carrega a base dos calculos
    conf = ConfCalculo.getInstance().getConfCalculo()

    form = FormDebito()
    empresas = get_empresas()
    debitos = get_debitos()
    form.empresa.choices = [(str(i),(empresa['fantasia'], empresa['cnpj'])) for i, empresa in enumerate(empresas)]

    if form.validate_on_submit():
        index = int(form.empresa.data)
        empresa = form.empresa.choices[index][1]
        result = Empresa.query.filter_by(cnpj=empresa[1]).first()
        
        debito = Debito(
            data_debito=date.today(),
            empresa=result
        )
        indice = result.indice
        valor_final = Debito.calculo_debito(indice, conf['base_debitos'])
        result.indice = valor_final

        db.session.add(result)
        db.session.add(debito)
        db.session.commit()

        form.empresa.data = ''
        debitos = get_debitos()

        return render_template('debito.html',form=form, debitos=debitos)

    return render_template('debito.html',form=form, debitos=debitos)

def get_empresas():
    empresas = Empresa.query.all()
    empresas_json = [empresa.to_json() for empresa in empresas]
    return empresas_json

def get_notas():
    notas = NotaFiscal.query.all()
    notas_json = [nota.to_json(nota.empresa.fantasia) for nota in notas ]
    return notas_json

def get_debitos():
    debitos = Debito.query.all()
    debitos_json = [debito.to_json(debito.empresa) for debito in debitos]
    return debitos_json
