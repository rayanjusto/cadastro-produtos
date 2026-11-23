import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect("produtos.db")

# Criar a tabela
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_produto (
        cd_produto INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_produto TEXT NOT NULL
    )
""")

conexao.commit()

print("Banco de dados conectado com sucesso!")


def incluir_produto():
    nome = input("Digite o nome do produto: ")

    if nome.strip() == "":
        print("O nome não pode ficar vazio!")
        return

    cursor.execute(
        "INSERT INTO tb_produto (nome_produto) VALUES (?)",
        (nome,)
    )

    conexao.commit()

    print("Produto cadastrado com sucesso!")


def consultar_produtos():
    cursor.execute("SELECT * FROM tb_produto")

    produtos = cursor.fetchall()

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("\n--- PRODUTOS CADASTRADOS ---")

    for produto in produtos:
        print(f"Código: {produto[0]} | Nome: {produto[1]}")


def alterar_produto():
    codigo = input("Digite o código do produto: ")

    nome = input("Digite o novo nome: ")

    if not nome.strip():
        print("O nome não pode ficar vazio!")
        return

    cursor.execute("""
        UPDATE tb_produto
        SET nome_produto = ?
        WHERE cd_produto = ?
    """, (nome, codigo))

    conexao.commit()

    if cursor.rowcount > 0:
        print("Produto alterado com sucesso!")
    else:
        print("Produto não encontrado.")


def excluir_produto():
    codigo = input("Digite o código do produto: ")

    cursor.execute("""
        DELETE FROM tb_produto
        WHERE cd_produto = ?
    """, (codigo,))

    conexao.commit()

    if cursor.rowcount > 0:
        print("Produto excluído com sucesso!")
    else:
        print("Produto não encontrado.")


def menu():
    while True:
        print("\n===== SISTEMA DE PRODUTOS =====")
        print("1 - Incluir produto")
        print("2 - Consultar produtos")
        print("3 - Alterar produto")
        print("4 - Excluir produto")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            incluir_produto()

        elif opcao == "2":
            consultar_produtos()

        elif opcao == "3":
            alterar_produto()

        elif opcao == "4":
            excluir_produto()

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida!")

menu()

conexao.close()