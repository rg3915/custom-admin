# Custom Admin Django

## Como desenvolver?

Baixe e rode o `setup.sh`.

```
wget https://raw.githubusercontent.com/rg3915/custom-admin/master/setup.sh
source setup.sh
```

Ou siga o passo a passo.

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute a migração
7. Crie um super usuário

```bash
git clone https://github.com/rg3915/custom-admin.git
cd custom-admin
python -m venv .venv
source .venv/bin/activate # Linux
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py migrate
python manage.py createsuperuser --username='admin' --email=''
```

## Features

* Alterando a tela de login