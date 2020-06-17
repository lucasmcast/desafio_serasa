import unittest
from app import create_app, db
from app.models import Empresa, NotaFiscal, Debito, ConfCalculoDB

class FlaskClientTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        ConfCalculoDB.insert_conf()
        self.client = self.app.test_client(use_cookies=True)
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_cadastro_page(self):
        response = self.client.get('/cadastro')
        self.assertEqual(response.status_code, 200)
    
    def test_notafiscal_page(self):
        response = self.client.get('/notaFiscal')
        self.assertEqual(response.status_code, 200)

    def test_debitos_page(self):
        response = self.client.get('/debitos')
        self.assertEqual(response.status_code, 200)