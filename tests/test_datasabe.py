import unittest
from datetime import date
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
    
    def test_insert_empresa(self):
        empresa = Empresa(
            fantasia="Empresa Teste",
            razao_social="Empresa Teste LTDA",
            cnpj="33.333.333/3333-33",
            indice=50
        )
        
        db.session.add(empresa)
        db.session.commit()

        r = Empresa.query.filter_by(cnpj="33.333.333/3333-33").first()
        self.assertIsNotNone(r)
    
        self.assertEqual(r.fantasia, "Empresa Teste")
        self.assertEqual(r.razao_social, "Empresa Teste LTDA")
        self.assertEqual(r.cnpj, "33.333.333/3333-33")
        self.assertEqual(r.indice, 50)
    
    def test_insert_notafiscal(self):
        date_today = date.today()
        empresa = Empresa(
            fantasia="Empresa Teste",
            razao_social="Empresa Teste LTDA",
            cnpj="33.333.333/3333-33",
            indice=50
        )
        
        db.session.add(empresa)
        db.session.commit()

        r = Empresa.query.filter_by(cnpj="33.333.333/3333-33").first()
        self.assertIsNotNone(r)

        notafiscal = NotaFiscal(
            numero_nota="25252525",
            empresa=r,
            data_emissao=date.today()
        )

        db.session.add(notafiscal)
        db.session.commit()

        r = NotaFiscal.query.filter_by(numero_nota="25252525").first()
        self.assertIsNotNone(r)
    
        self.assertEqual(r.numero_nota, "25252525")
        self.assertEqual(r.data_emissao, str(date_today))
        self.assertEqual(r.empresa, empresa)

    def test_insert_debito(self):
        date_today = date.today()
        empresa = Empresa(
            fantasia="Empresa Teste",
            razao_social="Empresa Teste LTDA",
            cnpj="33.333.333/3333-33",
            indice=50
        )
        
        db.session.add(empresa)
        db.session.commit()

        r = Empresa.query.filter_by(cnpj="33.333.333/3333-33").first()
        self.assertIsNotNone(r)

        debito = Debito(
            id_debito=65535,
            data_debito=date.today(),
            empresa=r,
        )

        db.session.add(debito)
        db.session.commit()

        r = Debito.query.filter_by(id_debito=65535).first()
        self.assertIsNotNone(r) 
        self.assertEqual(r.data_debito, str(date_today))
        self.assertEqual(r.empresa, empresa)

