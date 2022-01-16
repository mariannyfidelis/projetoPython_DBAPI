import MySQLdb

class FabricaConexao():
        
    @staticmethod
    def conectar():
        MySQLdb.paramstyle = "format"
        db = MySQLdb.connect(user="root", passwd="mysql", db="clientes", host="localhost", port=3306)
        print("Conexão com o Banco de dados MySQL realizada com sucesso !")
        return db
