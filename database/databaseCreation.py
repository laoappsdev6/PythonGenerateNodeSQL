import mysql.connector
from database.databaseConnection import DatabaseConnection
from model.message import Msg


class DatabaseCreation:

    @staticmethod
    def create(databaseName: str) -> bool:
        try:
            connServer = DatabaseConnection.connectServer()
            cursor = connServer.cursor()
            sql = "CREATE DATABASE IF NOT EXISTS {} character set utf8 collate utf8_general_ci".format(databaseName)
            cursor.execute(sql)
            cursor.close()
            connServer.close()
            return True
        except mysql.connector.Error as err:
            print(Msg.createDbFail, err)
            return False
