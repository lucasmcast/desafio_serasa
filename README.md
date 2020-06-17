# Desafio Serasa

Programa serada para novos desenvolvedores, criou o desafio para avaliar o nivel de conhecimento dos candidatos. O sistema é um classificador de empresas. Neste as empresas são classificadas com um índice de 1 a 100 representando a confiabilidade da empresa no mercado financeirto.

Considerando as regras para o cáculo:

- Cada nota fiscal emitida aumenta 2% a pontuação arredondando para baixo a partit da primeira casa decimal;

- Cada pendência financeira diminui em 4% a pontuação arredondando para cima a partir da primeira casa decimal;

## Documentação da API:

[Estrutura do documento](https://github.com/lucasmcast/desafio_serasa/wiki/Documenta%C3%A7%C3%A3o-da-API)

## Instalação

Requisitos:

- Python >= 3.6
- Python-venv
- Git

### Clonar repositório:

```bash
git clone https://github.com/lucasmcast/desafio_serasa.git
```

### Criar ambiente virtual:

```bash 
cd desafio_serasa/
python3 -m venv venv 
```

#### Ativando ambiente virtual:

Linux:

```bash 
source venv/bin/activate 
```

Windows:

```bash 
venv\Scripts\activate
```

### Instalação das dependências:

```bash
(venv) pip install -r requeriments/commons.txt
```

### Criando o banco de dados:

```bash 
(venv) flask deploy 
```

### Executando o projeto:

```bash 
flask run 
```

Endereço interno padrão para acessar a aplicação é http://127.0.0.1:5000

### Requisitos Minimos para o teste:

- [x] Precisa ter uma interface;
- [x] Precisa ter testes unitários;
- [x] Deve ter a documentação de setup e do funcionamento das APIs;

### Requisitos da aplicação:

- [x] Empresas Cadastradas;
- [x] A empresa deve ter um ID;
- [x] API para importar dados financeiros da empresa para o banco, como, quantidade de notas no mês e debitos;
- [x] Tela para o usuário importar dados das notas e debitos;
- [x] Criar um serviço para ler dados do banco e realizar os calculos;
- [x] Criar tela para apresentar o ranking com o índice das empresas cadastradas;
- [x] Cada  arquivo novo incluído no sistemas deve ser executado calculos.
