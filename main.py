#TODO 01 - Importar o pacote
import MySQLdb, cliente

#Formato ANSI C
MySQLdb.paramstyle = "format"

#TODO 02 - Configurando a conexão
db = MySQLdb.connect(user="root", passwd="mysql", db="clientes", host="localhost", port=3306)
print("Conexão com o Banco de dados MySQL realizada com sucesso !")

cursor = db.cursor()
cursor.execute("SELECT * FROM cliente")
print(cursor.fetchall())

cliente = cliente.Cliente("Joana", 35)
print("_________________________________")
listar_clientes()
inserir_cliente(cliente)
cursor.fetchall()
print("_________________________________")

#TODO 03 - Fechando a conexao
db.close()

