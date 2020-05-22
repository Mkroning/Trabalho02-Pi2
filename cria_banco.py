import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

cria_tabela = "CREATE TABLE IF NOT EXISTS veiculos (veiculo_id text PRIMARY KEY, modelo text, placa text, ano real, cor text, combustivel text, valor real)"

cursor.execute(cria_tabela)

connection.commit()
connection.close()