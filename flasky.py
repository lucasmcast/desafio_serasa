#Este modulo é o local em que está definida a instância da aplicação

import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    
from app import create_app
from app.models import db, Empresa, ConfCalculo, ConfCalculoDB
from sqlalchemy import MetaData
#A configuração será obtida da variavel de ambiente FLASK_CONFIG
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.app_context().push()

app.config


def is_tables_exist():
    """
    Função verifica se existe tabelas criadas no banco de dados
    return bool
    """
    metadata = MetaData(db.engine, reflect=True)
    tables = metadata.sorted_tables
    if len(tables) > 0:
        return True
    else:
        return False

if is_tables_exist():
    ConfCalculo()

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Empresa=Empresa, ConfCalculoDB=ConfCalculoDB)

@app.cli.command()
def deploy():
    """Criar o banco para a aplicação ser executada"""
    db.drop_all()
    db.create_all()
    ConfCalculoDB.insert_conf()

@app.cli.command()
def test():
    """Executar os testes"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)