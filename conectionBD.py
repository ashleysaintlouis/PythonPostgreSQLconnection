import mysql.connector
import datetime

lancamento = datetime.datetime(2017,11,13)

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="15021989A",
    database="lojaDeGames"
)

cursor = conexao.cursor()

# Corrigir a sintaxe da query SQL e fornecer os valores como uma tupla
query = """INSERT INTO clientes (nome, email, senha, data_nascimento, endereco, cidade, estado, cep, telefone)
           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

valores_cliente = ("Nicolson Saint-Louis", "Nicolsonsaintlouis989@gmail.com", "sua_senha", "1972-09-15", "Rua São Pedro", "Erechim", "SC", "89542-454", "485254122")

cursor.execute(query, valores_cliente)
conexao.commit()

query = """ INSERT INTO jogos (nome, tipoDeJogo, plataforma
data_lancamento, preco, quantidade, descricao)
VALUES (%s, %s, %s, %s, %s, %s, %s)"""

valores_jogo = ("Tenis", "Creed", "XBO 360", lancamento, 20, 50 ,"Tenis jogos")

cursor.execute(query, valores_jogo)
conexao.commit()

query = "SELECT * FROM jogos"
cursor.execute(query)
jogos = cursor.fretchall()

for jogo in jogos:
    print(jogo)

query = "UPDATE jogos SET descricao"
query += "%s WHERE id = %s"

valores_jogo = ("O primeiro franquia....",1)
cursor.execute(query, valores_jogo)
conexao.commit()


cursor.close()
conexao.close()
