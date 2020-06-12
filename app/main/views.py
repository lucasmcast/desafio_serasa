from flask import Flask, render_template, redirect, url_for
from datetime import date
from . import main
from .forms import FormEmpresa, FormNotaFiscal
from .. import db
from ..models import Empresa, NotaFiscal
import random
from pprint import pprint


notas = []

@main.route('/', methods=['GET', 'POST'])
def index():
    #ordena a lista de empresa do maior para o menor indice
    empresas = Empresa.query.all()
    empresas_json = [empresa.to_json() for empresa in empresas]

    empresas_json = sorted(empresas_json, key=lambda k: k['indice'], reverse=True)

    return render_template('index.html', empresas=empresas_json)
    
@main.route('/cadastro', methods=['GET','POST'])
def cadastro():

    form = FormEmpresa()
    empresas = get_empresas()

    if form.validate_on_submit():
        empresa = Empresa(
            fantasia=form.fantasia.data,
            razao_social=form.razao_social.data,
            cnpj=form.cnpj.data,
            email=form.email.data,
            indice=50
        )
        db.session.add(empresa)
        db.session.commit()

        form.fantasia.data = ''
        form.razao_social.data = ''
        form.cnpj.data = ''
        form.endereco.data = ''
        form.email.data = ''

        empresas = get_empresas()

        return render_template('cadastro_empresa.html', form=form, empresas=empresas)
    
    return render_template('cadastro_empresa.html', form=form, empresas=empresas)

@main.route('/notaFiscal', methods=['GET', 'POST'])
def nota_fiscal():
    form = FormNotaFiscal()
    empresas = get_empresas()
    notas = get_notas()
    form.empresa.choices = [(str(i), empresa['fantasia']) for i, empresa in enumerate(empresas)]

    if form.validate_on_submit():
        index = int(form.empresa.data)
        numero_nota = random.randint(1, 123456)
        empresa = form.empresa.choices[index][1]
        result = Empresa.query.filter_by(fantasia=empresa).first()
        
        nota = NotaFiscal(
            numero_nota=numero_nota,
            data_emisao=date.today(),
            empresa=result
        )
        indice = result.indice
        valor_final = NotaFiscal.calculo_nota_fiscal(indice)
        result.indice = valor_final

        db.session.add(result)
        db.session.add(nota)
        db.session.commit()

        form.empresa.data = ''
        notas = get_notas()

        return render_template('nota_fiscal.html', form=form, notas=notas)

    return render_template('nota_fiscal.html', form=form, notas=notas)

@main.route('/debitos')
def debito():
    return render_template('debito.html')

def get_empresas():
    empresas = Empresa.query.all()
    empresas_json = [empresa.to_json() for empresa in empresas]
    return empresas_json

def get_notas():
    notas = NotaFiscal.query.all()
    # for nota in notas:
    #     print(nota.empresa.fantasia)

    notas_json = [nota.to_json(nota.empresa.fantasia) for nota in notas ]
    return notas_json

