## Como criar virtual

```sh
# executar mesmo nivel pasta app
python -m venv ./venv
```

## Como habilitar virtual

```sh
# executar mesmo nivel pasta app
.\venv\Scripts\Activate
```

## Instalando dependencias

```sh
pip install Flask flask_migrate flask_marshmallow marshmallow_sqlalchemy flask-jwt-extended passlib psycopg2 python-dotenv redis  flask-session 
```

## Como rodar esse projeto

```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

flask run
```

## Como fazer as migrações

```sh
flask db init
flask db migrate
flask db upgrade
```

## Como rodar os testes e obter cobertura

```sh
# gera o report e roda os testes UNITARIOS
coverage run --source=app --module unittest  discover -s tests/auto/unit -v
# gera o report e roda os testes INTEGRADOS
coverage run --source=app --module unittest  discover -s tests/auto/int -v

# mostra um resumo da cobertura em shell
coverage report
# gera o path '/htmlcov' com htmls estáticos da cobertura
coverage html
```

## Como rodar sqlacodegen para rever bdatabase

```sh
sqlacodegen postgresql://postgres:postgres@localhost:5432/flaskapi --outfile x.py --
noviews
```
