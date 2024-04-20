"""
to-order-pizza README

## Configuração das migrations para criação do banco de dados:

1. Instale o alembic usando:
    ```
    pip install alembic
    ```

2. Inicialize o alembic:
    ```
    alembic init migrations
    ```

3. Dentro do arquivo alembic.ini, altere o valor de `script_location` para o nome criado no init. Por exemplo:
    ```
    script_location = migrations
    ```

4. Dentro da pasta "migrations" que foi gerada, abra o arquivo .env e importe a URL do seu banco de dados e o objeto Base das entidades de tabela que deseja criar no banco. Por exemplo:
    ```python
    from gateways.connection import connection_db_url
    from domain.entity.entity import Base

    config = context.config
    config.set_main_option('sqlalchemy.url', connection_db_url)
    ```

5. Gere uma nova revisão do banco de dados usando o comando:
    ```
    alembic revision --autogenerate -m "initial"
    ```

6. Aplique as migrações geradas para criar as tabelas no banco de dados usando o comando:
    ```
    alembic upgrade head
    ```

## Executando o aplicativo:

Para executar o aplicativo, siga estes passos:

1. Certifique-se de ter Python e todas as dependências instaladas.
2. Navegue até o diretório raiz do projeto.
3. Execute o aplicativo usando o comando:
    ```
    python main.py
    ```

O aplicativo será iniciado e estará disponível em http://localhost:5000.

## Desenvolvimento adicional:

Para desenvolvimento adicional, você pode considerar as seguintes etapas:

- Implementar novas funcionalidades ou aprimorar as existentes no código-fonte.
- Documentar o código usando docstrings e comentários claros para facilitar a compreensão e manutenção.
- Realizar testes unitários e de integração para garantir a robustez do aplicativo.
- Gerenciar o versionamento do código usando um sistema de controle de versão, como Git.



## BackEnd Routes
### FrontEnd Routes
Usando método no Header POST http://localhost:8080
- `/pizza`: Rota para cadastrar uma nova pizza.
- `/pasta`: Rota para cadastrar uma nova massa.

Usando método no Header GET http://localhost:8080
- `/pizza`: Rota para Buscar pizza.
- `/pasta`: Rota para Buscar  massa.


Usando método no Header GET http://localhost:8080/id
- `/pizza`: Rota para Buscar por id uma pizza.
- `/pasta`: Rota para Buscar por id uma massa.

Usando método no Header PUT http://localhost:8080/id
- `/pizza`: Rota para Editar por id uma pizza.
- `/pasta`: Rota para Editar por id uma massa.

Usando método no Header PUT http://localhost:8080/id
- `/pizza`: Rota para inativar por id uma pizza.
- `/pasta`: Rota para inativar por id uma massa.
- esse método inativa ou ativa, para não perder rastreabilidade, não excluo do banco