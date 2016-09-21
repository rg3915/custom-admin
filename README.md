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
python manage.py createsuperuser --email='nome@email.com'
```

## Features

### Alterando a tela de login

Em `settings.py` defina sua APP como primeiro em INSTALLED_APPS.

```python
INSTALLED_APPS = [
    'myproject.core',
    'django.contrib.admin',
    ...
```

Na pasta myproject/core/ crie a pasta templates/admin/.

Dentro do seu ambiente virtual procure por django/contrib/admin/templates/admin/login.html

Ou acesse https://github.com/django/django/tree/master/django/contrib/admin/templates/admin/ .

E coloque dentro da sua pasta, ficando assim:

`myproject/core/templates/admin/login.html`

A partir dai você pode alterar sua tela de login como desejar.


### Login personalizado com email e senha

A partir da documentação [Customizing authentication in Django](https://docs.djangoproject.com/en/1.10/topics/auth/customizing/) vamos fazer login com `email` e `senha`, ao invés de username.

Em `settings.py` defina `AUTH_USER_MODEL = 'myauth.User'`.

Crie uma App chamada `myauth`.

```
python manage.py startapp myauth
```

Defina em `INSTALLED_APPS`.

```python
INSTALLED_APPS = [
    # my apps
    'myproject.core',
    'django.contrib.admin',
    # ...
    'myproject.myauth',
]
```

#### Testes

Vamos criar os testes:

```bash
mkdir myauth/tests
touch myauth/tests/{__init__.py,test_backends.py,test_custom_user.py}
```

[test_backends.py](myproject/myauth/tests/test_backends.py)

[test_custom_user.py](myproject/myauth/tests/test_custom_user.py)


#### Modelo

A maioria dos tutoriais, inclusive a documentação cria a nova classe herdando de [AbstractBaseUser](https://github.com/django/django/blob/master/django/contrib/auth/base_user.py#L52) mas ele só contém os campos de autenticação, `password` e `last_login`. O modelo [AbstractUser](https://github.com/django/django/blob/master/django/contrib/auth/models.py#L297) é mais completo, ele contém todos os campos conhecidos de `User`, que são: `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active` e `date_joined`.

```python
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


class User(AbstractUser):
    email = models.EmailField(unique=True, db_index=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'
        ordering = ('email',)

    def __str__(self):
        return self.get_full_name()

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    @property
    def is_staff(self):
        return True
```

Seguindo a [documentação](https://docs.djangoproject.com/en/1.10/topics/auth/customizing/#a-full-example) vamos criar um `UserManager`, mas eu preferi fazer isso num arquivo separado:

[managers.py](myproject/myauth/managers.py)


#### backends

[backends.py](myproject/myauth/backends.py) é o arquivo que faz a autenticação.

#### Formulários

Em [forms.py](myproject/myauth/forms.py) criamos `UserCreationForm` e `UserChangeForm`.


#### Admin

Em [admins.py](myproject/myauth/admins.py) definimos `UserAdmin` herdando de `BaseUserAdmin`.


#### Migração

Agora rode

```bash
python manage.py makemigrations myauth
python manage.py migrate
```

**Nota:** no Django 1.9.2 estava dando o seguinte erro:

```
django.core.exceptions.FieldError: Local field 'email' in class 'User' clashes with field of similar name from base class 'AbstractUser'
```

Mas no Django 1.10 o erro não ocorreu (talvez por isso que a maioria dos tutoriais herdam de `AbstractBaseUser`).

```bash
python manage.py test
python manage.py createsuperuser
```

Para finalizar edite `settings.py`

```python
'myproject.myauth.apps.MyauthConfig',
```

E edite `myauth/apps.py`

```python
class MyauthConfig(AppConfig):
    name = 'myproject.myauth'
    verbose_name = 'Autenticação Usuários'
```