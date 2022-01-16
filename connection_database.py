import MySQLdb
import configparser

class FabricaConexao():

    @staticmethod
    def conectar():
        MySQLdb.paramstyle = "format"
        config = configparser.ConfigParser()
        config.read('config.ini')
        db = MySQLdb.connect(user=config['DATABASE']['user'],
                             passwd=config['DATABASE']['passwd'],
                             db=config['DATABASE']['db'],
                             host=config['DATABASE']['host'], 
                             port=int(config['DATABASE']['port']))
        print("Conexão com o Banco de dados MySQL realizada com sucesso !")
        return db
