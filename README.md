# desafio-tech-django

Desafio Tech (Automação)

Construir pelo menos dois endpoints utilizando Django:
  - Cadastrar usuário, fornecendo o login, senha e data de nascimento
  - Senha deixar como opcional, se não fornecido gerar uma senha aleatória.
  - Consultar usuários cadastrados.

## Dependencies
Python 3.9.11

python venv

## Start Project
```
python -m venv venv
.\venv\Scripts\activate.bat
pip install -r Requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## API Usage Examples

### Get all users
#### GET -  http://127.0.0.1:8000/users
#### Response
```
[
    {
        "id_user": "63945c3e-4fb5-46f3-bda2-ed80fc643c4e",
        "name": "Ana Júlia",
        "username": "Musya",
        "birthdate": "28/02/1960",
        "password": "tk3HpdvjeJwCwYfnqrpnexBKGcZkas"
    },
    {
        "id_user": "9afc55d2-ac28-42f8-83f1-680c314ffda6",
        "name": "Lucas",
        "username": "luquinha",
        "birthdate": "10/03/2002",
        "password": "whuiwhruw"
    }
]

```

### Get specific user
#### GET -  http://127.0.0.1:8000/users/63945c3e-4fb5-46f3-bda2-ed80fc643c4e
#### Response
```
{
    "id_user": "63945c3e-4fb5-46f3-bda2-ed80fc643c4e",
    "name": "Ana Júlia",
    "username": "Musya",
    "birthdate": "28/02/1960",
    "password": "tk3HpdvjeJwCwYfnqrpnexBKGcZkas"
}
```

### Create new user
#### POST - http://127.0.0.1:8000/users/create/
#### Request Body
```
{
    "name": "Lucas",
    "username": "luquinha",
    "birthdate": "10/03/2002",
    "password": "whuiwhruw"
}
```

##### Response
Status: 201 Created
```
{
    "id_user": "9afc55d2-ac28-42f8-83f1-680c314ffda6",
    "name": "Lucas",
    "username": "luquinha",
    "birthdate": "10/03/2002",
    "password": "whuiwhruw"
}
```
