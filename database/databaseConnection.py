import mysql.connector
from config.config import MyConfig
from model.message import Msg


class DatabaseConnection:

    @staticmethod
    def connectServer():
        try:
            return mysql.connector.connect(
                host=MyConfig.dbHost,
                user=MyConfig.dbUser,
                password=MyConfig.dbPass
            )
        except mysql.connector.Error as err:
            print(Msg.svConnectFail, err)
            return False

    @staticmethod
    def connectDatabase(databaseName:str):
        try:
            return mysql.connector.connect(
                host=MyConfig.dbHost,
                user=MyConfig.dbUser,
                password=MyConfig.dbPass,
                database=databaseName
            )
        except mysql.connector.Error as err:
            print(Msg.dbConnectFail, err)
            return False