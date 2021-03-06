# Eventex


Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/HildePedroni/eventex.svg?branch=master)](https://travis-ci.org/HildePedroni/eventex)
[![Code Health](https://landscape.io/github/HildePedroni/eventex/master/landscape.svg?style=flat)](https://landscape.io/github/HildePedroni/eventex/master)



## Como desenvolver?
1. Clone o repositorio
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os teste.


````console
git clone https://github.com/HildePedroni/eventex.git
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test

````

## Como fazer o deploy?

1. Crie uma instaância no heroku
2. Envie as configurações para o heroku
3. defina uma SCRET_KEY segura
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku

````console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
#configura o email
git push heroku master --force
````