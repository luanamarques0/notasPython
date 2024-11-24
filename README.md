# NotasPython 

**NotasPython** é uma aplicação de linha de comando em Python e MySQL para gerenciamento de notas(Anotações). Permite criar usuários, notas  e exibir todas as notas.


# 🚀 Funcionalidades

- **Criar usuários**: Registrar novos usuários no sistema a partir do nome.
- **Adicionar notas**: Cria notas que são associadas a um usuário já existente, com título, e escopo.
- **Exibir notas**:O usuário poderá vizualizar todas as notas que adicionou ao sistema, incluindo a sua data de criação.


## 🛠️ Tecnologias Utilizadas

- **Python 3.12.2**
- **MySQL**
- **MySQL Connector for Python**
- **Python-dotenv**
- **Virtual Environment (venv)**


## 📋 Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:

- **Python 3.8+**
- **MySQL**
- **pip** 


## 🔧 Como Configurar o Ambiente

1. **Clone o repositório**:

2. **Crie e ative o ambiente virtual (venv)**:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure as variáveis de ambiente**:
   Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
    ```dotenv
    HOST_DB=Seu_host
    USER_DB=Seu_usuario
    PASSWORD_DB=Sua_senha
    ```

5. **Certifique-se de que o MySQL está em execução**.



## ▶️ Como Executar o Projeto

**Certifique-sede configurar o arquivo `.env` corretamente, configure antes de executar o programa** 

1. **Inicie o programa**:
    ```bash
    python app.py
    ```

2. **Use o menu interativo**:
    ```
       Bem-vindo ao NotasPython!
    -------------------------------
        Escolha uma das opções:
         1 - Criar novo usuário
         2 - Criar uma nova nota
         3 - Exibir todas as notas
         4 - Sair
    ```


## 🗂️ Estrutura do Projeto

```plaintext
NotasPython/
│
├── app.py               # Arquivo principal que gerencia o menu interativo
├── connDB.py            # Contém as funções para conexão com o banco de dados e manipulação dos dados
├── requirements.txt     # Dependências do projeto
├── .env                 # Variáveis de ambiente (não incluído no repositório)
└── README.md            # Documentação do projeto
```

## Melhorias Futuras 💡

- Permitir edição e exclusão de notas.
- Melhorar a interface do menu para torná-la mais interativa.

------------------------------------------

##  🧡 Assinatura 

Feito por **Luana Marques** 

![Logo](https://drive.google.com/uc?id=1OZeJ78qrs7nUiGCxgxdnS0blQkdjhnYO)


