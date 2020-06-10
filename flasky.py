#Este modulo é o local em que está definida a instância da aplicação

import os
from app import create_app

#A configuração será obtida da variavel de ambiente FLASK_CONFIG
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.shell_context_processor
def make_shell_context():
    pass