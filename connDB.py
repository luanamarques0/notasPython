from mysql.connector import Error
from dotenv import load_dotenv
import mysql.connector
import os
from datetime import date

# Carregar variáveis de ambiente
load_dotenv(".env")
host_db = os.getenv("HOST_DB")
user_db = os.getenv("USER_DB")
password_db = os.getenv("PASSWORD_DB")

connection = None
try:
    # Conexão com o banco de dados
    connection = mysql.connector.connect(
        host=host_db,
        user=user_db,
        password=password_db,
        use_pure=True
    )

    if connection.is_connected():
        my_cursor = connection.cursor()

        # Criação do schema e tabelas
        my_cursor.execute("CREATE SCHEMA IF NOT EXISTS Python_notes")
        my_cursor.execute("USE Python_notes")

        #Schema tabela do usuário
        user_table = """
        CREATE TABLE IF NOT EXISTS user (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL UNIQUE
        );
        """
        #Schema da tabela das notas
        notes_table = """
        CREATE TABLE IF NOT EXISTS notes (
            id_notes INT AUTO_INCREMENT PRIMARY KEY,
            id_user INT NOT NULL,
            date_ DATE NOT NULL,
            titulo VARCHAR(100),
            body_note VARCHAR(500),
            FOREIGN KEY (id_user) REFERENCES user(id)
        );
        """
        my_cursor.execute(user_table)
        my_cursor.execute(notes_table)
        connection.commit()
        print("Sucesso na criação do schema e das tabelas")

except Error as err:
    print(f"Erro na conexão ou criação do banco de dados: {err}")


############### Funções ###############
def create_user(nome_user):
    try:
        my_cursor.execute("SELECT name FROM user WHERE name = %s;", (nome_user,))
        result = my_cursor.fetchone()

        if result:
            print("Usuário já existe.")
        else:
            my_cursor.execute("INSERT INTO user (name) VALUES (%s);", (nome_user,))
            connection.commit()
            print("Usuário criado com sucesso!")
    except Error as err:
        print(f"Erro ao criar usuário: {err}")


def create_note(nome_user, titulo, note):
    try:
        my_cursor.execute("SELECT id FROM user WHERE name = %s;", (nome_user,))
        result = my_cursor.fetchone()

        if result:
            id_user = result[0]
            data_atual = date.today()
            my_cursor.execute(
                "INSERT INTO notes (id_user, date_, titulo, body_note) VALUES (%s, %s, %s, %s);",
                (id_user, data_atual, titulo, note)
            )
            connection.commit()
            print("Nota adicionada com sucesso!")
        else:
            print("Usuário não encontrado. Verifique as informações.")
    except Error as err:
        print(f"Erro ao criar nota: {err}")


def exibir_notes(nome_user):
    try:
        my_cursor.execute("SELECT id FROM user WHERE name = %s;", (nome_user,))
        result = my_cursor.fetchone()

        if result:
            id_user = result[0]
            my_cursor.execute(
                "SELECT titulo, body_note, date_ FROM notes WHERE id_user = %s;",
                (id_user,)
            )
            notas = my_cursor.fetchall()

            if notas:
                print(f"\n--- Notas de {nome_user} ---")
                for i, nota in enumerate(notas, start=1):
                    
                    print(f"""
                    ============================
                    Nota {i} - {nota[0]}
                    ============================
                    {nota[1]}

                    ----------------------------
                    Data: {nota[2]}
                    ============================
                    """)
            else:
                print("Nenhuma nota encontrada para este usuário.")
        else:
            print("Usuário não encontrado.")
    except Error as err:
        print(f"Erro ao exibir notas: {err}")
