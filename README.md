# Instruções para instalação do projeto

## 1. Primeiro de tudo, faça o clone

```shell
  git clone https://github.com/felipee123/Denuncia.git
```

## 2. Crie uma virtual env com o python

Abra seu terminal e navegue até o projeto que acabou de clonar

```shell
  cd Denuncia
```

Em seguida, use o comando:

```shell
  python -m venv venv
```

Com esse comando, você acabou de criar uma virtual env cahamada **venv**.

### 2.1. Ativando a virtual env

Se estiver usando Windows, basta usar o comando a seguir no seu terminal:

```shell
  .\venv\Scripts\Activate.ps1
```

Caso esteja utilizando Linux ou MacOS:

```shell
  source venv/bin/activate
```

## 3. Instalar os libs

Para instalar as bibliotecas/frameworks, basta utilizar o comando:

```shell
  pip install -r requirements.txt
```

## 4. Preparando para rodar o projeto

Antes de rodar o projeto, é preciso criar as migrations. Para isso, execute os seguintes comandos:

Supondo que você está dentro da pasta 'Denuncia', vamos criar as migrations

```shell
  python manage.py makemigrations
```

E por fim, executar as migrations criadas

```shell
  python manage.py migrate
```

Pronto, estamos prontos para rodar o projeto.

## 5. Rodando o projeto

Para rodar o projeto, basta executar:

```shell
  python manage.py runserver
```

O projeto será iniciado em **http://127.0.0.1:8000**
