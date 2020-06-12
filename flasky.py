#Este modulo é o local em que está definida a instância da aplicação

import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    
from app import create_app
from app.models import db, Empresa

#A configuração será obtida da variavel de ambiente FLASK_CONFIG
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.config

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Empresa=Empresa)