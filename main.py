from utils.database_utils import create_tables


if __name__ == "__main__":
    print("Criando o Banco de Dados...")
    print("Criando as tabelas...")
    create_tables()
    print("Criando as chaves estrangeiras...")
    print("Sucesso.")
