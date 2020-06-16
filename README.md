# Desafio Serasa

Programa serada para novos desenvolvedores, criou o desafio para avaliar o nivel de conhecimento dos candidatos. O sistema é um classificador de empresas. Neste as empresas são classificadas com um índice de 1 a 100 representando a confiabilidade da empresa no mercado financeirto.

Considerando as regras para o cáculo:

- Cada nota fiscal emitida aumenta 2% a pontuação arredondando para baixo a partit da primeira casa decimal;

- Cada pendência financeira diminui em 4% a pontuação arredondando para cima a partir da primeira casa decimal;

## Documentação da API:

link para documentação

## Instalação

Requisitos:

- Python >= 3.6
- Python-venv
- Git

### Clonar repositório:

```git clone https://github.com/lucasmcast/desafio_serasa.git```

### Criar ambiente virtual:

``` cd desafio_serasa/ ```
``` python3 -m venv venv ```

#### Ativando ambiente virtual:

Linux:

``` source venv/bin/activate ```

Windows:

``` venv\Scripts\activate```

### Instalação das dependências:

```(venv) pip install -r requeriments/commons.txt```

### Criando o banco de dados:

``` (venv) flask deploy ```

### Executando o projeto:

``` flask run ```

Endereço interno padrão para acessar a aplicação é http://127.0.0.1:5000

### Requisitos Minimos para o teste:

- [x] Precisa ter uma interface;
- [ ] Precisa ter testes unitários;
- [ ] Deve ter a documentação de setup e do funcionamento das APIs;

### Requisitos da aplicação:

- [x] Empresas Cadastradas;
- [x] A empresa deve ter um ID;
- [ ] API para importar dados financeiros da empresa para o banco, como, quantidade de notas no mês e debitos;
- [x] Tela para o usuário importar dados das notas e debitos;
- [x] Criar um serviço para ler dados do banco e realizar os calculos;
- [x] Criar tela para apresentar o ranking com o índice das empresas cadastradas;
- [x] Cada  arquivo novo incluído no sistemas deve ser executado calculos.
