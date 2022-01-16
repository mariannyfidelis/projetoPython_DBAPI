from connection_database import FabricaConexao

class ClienteRepository():

    @staticmethod
    def listar_clientes():
        fabrica = FabricaConexao.conectar()
        try:
            cursor = fabrica.cursor()
            cursor.execute("SELECT * FROM cliente")
            print(cursor.fetchall())
        finally:
            fabrica.close()
    
    @staticmethod
    def inserir_cliente(cliente):
        fabrica = FabricaConexao.conectar()
        try:
            cursor = fabrica.cursor()
            cursor.execute("INSERT INTO cliente (nome, idade) VALUES (%s,%s)", (cliente.nome, cliente.idade))
            fabrica.commit()
        finally:
            fabrica.close()

    @staticmethod
    def atualizar_cliente(id_Cliente, cliente):
        fabrica = FabricaConexao.conectar()
        try:
            cursor = fabrica.cursor()
            cursor.execute(f"UPDATE cliente SET nome='{cliente.nome}', idade={cliente.idade} WHERE idCliente={id_Cliente};")
            fabrica.commit()
        finally:
            fabrica.close()

    @staticmethod
    def remover_cliente(id_Cliente):
        fabrica = FabricaConexao.conectar()
        try:
            cursor = fabrica.cursor()
            cursor.execute(f"DELETE FROM cliente WHERE idCliente={id_Cliente};")
            fabrica.commit()
        finally:
            fabrica.close()
#======================================================================================================            
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