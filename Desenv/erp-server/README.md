# EPR-SERVER

## Criando ambiente de desenvolvimento

---

1. Criar ambiente virtual

   ```sh
   # executar mesmo nivel pasta app
   python -m venv ./venv
   ```

2. Habilitar ambiente virtual

   ```sh
   # win executar mesmo nivel pasta app
   .\venv\Scripts\Activate
   ```

   ```sh
   # linux executar mesmo nivel pasta app
   source venv/bin/activate
   ```

## Executando o projeto

---

1. Instalando dependências
   ```
   pip install -r requiriments.txt
   ```
2. Executando o projeto em modo de desenvolvimento
   ```
   flask run
   ```

## Migrações

---

1. As migraçoẽs devem ser criadas dentro da pasta `migrations/versions` com nome de arquivos em ordem cronológica

2. Executando as migraçoẽs
   ```
   flask db upgrade
   ```
3. Exemplo de execução de uma migration específica
   ```
   flask db upgrade 202211100921002
   ```

## Executar CLI (Terminal)

---

1. Quando comando CLI e executado no flask aplicação inteira e startada devido uso do contexto geral

   ```sh
   # cli = Grupo da comando
   # test_cli = Nome comando dentro grupo
   # xxx = parametro para execucao do comando test1_print

   flask cli test_cli xxx
   ```

   - Exemplo no arquivo `app/configs/config_cli.py`

## Testes

---

1. Executando testes por cenário sendo a variável `TESTS_SCENARY` responsável por filtrar os cenários

```sh

--All
flask db upgrade

--Unica
flask db upgrade 202211301615003
```

## Como limpar cache Redis

```sh
redis-cli -a redis123 FLUSHDB
```
