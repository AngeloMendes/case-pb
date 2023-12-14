## Case Engenheiro de MLOps

API em Python utilizando fast-api

### Dependências
- [Docker](https://docs.docker.com/engine/install/)
- pipenv //pip install pipenv

### Reprodução
- Executando pelo container Docker

    ```
    docker build -t case .
    docker run --name case -p 8000:8000 case
    Acesso em: http://127.0.0.1:8000/docs
    ```
- Executando localmente
    
    Necessário ter Python na versão 3.8 instalada
    ```
    pipenv install
    pipenv shell
    python src/main.py
    Acesso em: http://127.0.0.1:8000/docs
    ```

### Testes
- Teste funcional
    ```
    pytest tests/    
    ```    
- Teste de carga
    ```
    locust tests/load.py
    Acesso em: http://127.0.0.1:8000/docs
    ```