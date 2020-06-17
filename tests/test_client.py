import unittest
from app import create_app, db
from app.models import Empresa, NotaFiscal, Debito

class FlaskClientTestCase(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_home_page(self):
        pass