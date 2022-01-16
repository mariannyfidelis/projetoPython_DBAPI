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


def listar_clientes():
    cursor.execute("SELECT * FROM cliente")
    print(cursor.fetchall())
    

def inserir_cliente(cliente):
    cursor.execute("INSERT INTO cliente (nome, idade) VALUES (%s,%s)", (cliente.nome, cliente.idade))
    db.commit();

def atualizar_cliente(id_Cliente, cliente):
    cursor.execute(f"UPDATE cliente SET nome='{cliente.nome}', idade={cliente.idade} WHERE idCliente={id_Cliente};")

def remover_cliente(id_Cliente):
    cursor.execute(f"DELETE FROM cliente WHERE idCliente={id_Cliente};")

def inserirCliente(nome, idade, cursor):
    cursor.execute(f"INSERT INTO cliente (nome, idade) VALUES ('{nome}', {idade});")
def atualizarCliente(idCliente,nome, idade, cursor):
    cursor.execute(f"UPDATE cliente SET nome='{nome}', idade={idade} WHERE idCliente={idCliente};")
def deletarCliente(idCliente, cursor):
    cursor.execute(f"DELETE FROM cliente WHERE idCliente={idCliente};")
def simularTransacaoCommitRollback(nome, idade, cursor, db):
    try:
        print("iniciando uma transação ...")
        db.begin()
        print("executando o INSERT INTO cliente ...")
        cursor.execute(f"INSERT INTO cliente (nomes, idade) VALUES ('{nome}', {idade});")
        print("realizando o commit no BD MySQL ...")
        db.commit()
    except:
        print("realizando o rollback devido uma exception ...")
        db.rollback()
def evitarSQLInjection(nome, idade, idCliente, cursor, db):
    cursor.execute("UPDATE cliente SET nome=%s, idade=%s WHERE idCliente=%s",(nome,idade,idCliente,))
    db.commit();
def executarVariasInsercoes(cursor, db):
    cursor.executemany("INSERT INTO cliente (nome, idade) VALUES (%s,%s)",
        #Cada tupla representa uma Inserção
        {
            ("Ana", 40),
            ("Maria", 50),
            ("Val", 34),
        }
    )

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
deletarCliente(10, cursor)
print(cursor.fetchall())
db.commit();
print(cursor.fetchall())

simularTransacaoCommitRollback("Tavares", 55, cursor, db)

nome = "José Sena"
idade= 35
idCliente = 11
cursor.execute("UPDATE cliente SET nome=%s, idade=%s WHERE idCliente=%s",(nome,idade,idCliente,))
db.commit();

evitarSQLInjection("Carlos Fontes", 38, 11, cursor, db)

executarVariasInsercoes(cursor, db)
db.commit();
"""
cliente = cliente.Cliente("Joana", 35)
print("_________________________________")
listar_clientes()
inserir_cliente(cliente)
cursor.fetchall()
print("_________________________________")
#TODO 03 - Fechando a conexao
db.close()

