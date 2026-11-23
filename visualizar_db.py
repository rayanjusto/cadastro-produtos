
import sqlite3

conexao = sqlite3.connect("produtos.db")
cursor = conexao.cursor()

# Consultar os produtos cadastrados
cursor.execute("SELECT * FROM tb_produto")

produtos = cursor.fetchall()

print("\n=== BANCO DE DADOS ===")
print("Tabela: tb_produto")
print("Código | Nome do produto")

for produto in produtos:
    print(f"{produto[0]} | {produto[1]}")

conexao.close()
