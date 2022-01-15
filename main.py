#TODO 01 - Importar o pacote
import MySQLdb

def inserirCliente(nome, idade, cursor):
    cursor.execute(f"INSERT INTO cliente (nome, idade) VALUES ('{nome}', {idade});")

def atualizarCliente(idCliente,nome, idade, cursor):
    cursor.execute(f"UPDATE cliente SET nome='{nome}', idade={idade} WHERE idCliente={idCliente};")

def deletarCliente(idCliente, cursor):
    cursor.execute(f"DELETE FROM cliente WHERE idCliente={idCliente};")

#TODO 02 - Configurando a conexão
db = MySQLdb.connect(user="root", passwd="mysql", db="clientes", host="localhost", port=3306)

print("Conexão realizada com sucesso !")

cursor = db.cursor()
cursor.execute("SELECT * FROM cliente")
print(cursor.fetchall())

"""
inserirCliente("Junior", 32, cursor)
cursor.execute("SELECT * FROM cliente")
print(cursor.fetchall())
db.commit();
"""
"""
-------------------------------------------------
atualizarCliente(7,"José Júnior", 34, cursor)
cursor.execute("SELECT * FROM cliente")
print(cursor.fetchall())

#TODO 04 - Persistindo os dados no banco de dados
db.commit();
-------------------------------------------------
"""

deletarCliente(10, cursor)
db.commit();

#TODO 03 - Fechando a conexao
db.close()