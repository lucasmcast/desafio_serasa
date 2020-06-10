# Estrutura Básica de um Projeto Flask

> Embora ter uma aplicação web pequena armazenada em um único arquivo de script possa ser muito conviniente, é importante que a estrutura do projeto seja organizada. Deste modo, caso a aplicação venha se tornar mais complexa, a preocupação de organizar trará facilidade na manutenção do códico.

Esse repositório não convém ser instalado, servindo apenas para ser clonado como um modelo no inicio de algum projeto flask, sem se preocupar em fazer as configurações iniciais ou pensar em uma estrutura. Claro que requer melhorias, mas ja é um inicio para começar a dar vida ao projeto. A estrutura foi obtida pelo livro "Desenvolvendo Web com Flask" com algumas modificações.

```
|- projeto_flask/
    |- app/
        |- templates/
        |- static/
        |- main/
            |- __init__.py
            |- errors.py
            |- forms.py
            |- views.py
        |- __init__.py
        |- email.py
        |- models.py
    |- migrations/
    |- tests/
        |- test*.py
    |- venv/
    |- requerements.txt
    |- config.py
    |- flasky.py
```

A estrutura tem quatro pastas de nível mais alto

* A aplocação Flask está em um pacote de nome genérico _apps_
* A pasta _migrations_ contém os script de manutenção de banco de dados.
* Os teste de unidade são escritos em um pacote _tests_
* A pasta _venv_ contém o ambiente virtual Python.
* _requerements.txt_ contém as depêndencias do pacote.
* _config.py_ armazena os parâmetros de configuração
* _flasky.py_ define a instância da aplicação flask.
