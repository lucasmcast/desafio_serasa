import unittest
from app import create_app, db
from app.models import Empresa, NotaFiscal, Debito, ConfCalculoDB, ConfCalculo

class CalculoTestCase(unittest.TestCase):
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
    
    def test_calculo_nota(self):
        conf = ConfCalculo.getInstance().getConfCalculo()
        indice = 50
        valor_final = NotaFiscal.calculo_nota_fiscal(indice, conf['base_nota'])
        self.assertEqual(valor_final, 51)
    
    def test_calculo_debito(self):
        conf = ConfCalculo.getInstance().getConfCalculo()
        indice = 56
        valor_final = Debito.calculo_debito(indice, conf['base_debitos'])
        self.assertEqual(valor_final, 54)

