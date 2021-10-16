import mysql.connector
from database.databaseConnection import DatabaseConnection
from model.message import Msg
from model.name import Name
from model.status import DBSync


class TableCreation:

    @staticmethod
    def create(databaseName: str, tableDetail: dict) -> bool:
        try:
            connDb = DatabaseConnection.connectDatabase(databaseName)
            cursor = connDb.cursor()

            tableKey = tableDetail.keys()
            for tableName in tableKey:
                tableField = tableDetail[tableName][Name.field]
                setting = tableDetail[tableName][Name.setting]
                mySync = setting[Name.dbSync]

                if mySync == DBSync.notExist:
                    myField = ""
                    for fieldName in tableField:
                        dataType = tableField[fieldName]
                        myField = myField + fieldName + " " + dataType + ","

                    fieldFormat = myField[0:len(myField) - 1]

                    sql = f"CREATE TABLE IF NOT EXISTS {tableName} ({fieldFormat}) default charset=utf8;"
                    cursor.execute(sql)

                if mySync == DBSync.replace:
                    myField = ""
                    for fieldName in tableField:
                        dataType = tableField[fieldName]
                        myField = myField + fieldName + " " + dataType + ","

                    fieldFormat = myField[0:len(myField) - 1]

                    sqlDrop = f"DROP TABLE IF EXISTS {tableName}"
                    cursor.execute(sqlDrop)

                    sql = f"CREATE TABLE IF NOT EXISTS {tableName} ({fieldFormat}) default charset=utf8;"
                    cursor.execute(sql)

                if mySync == DBSync.alter:

                    myField = ""
                    for fieldName in tableField:
                        dataType = tableField[fieldName]
                        if fieldName != "id":
                            myField = myField + " modify " + fieldName + " " + dataType + ","

                        fieldFormat = myField[0:len(myField) - 1]

                    sql = f"ALTER TABLE {tableName} {fieldFormat} "
                    print(sql)
                    cursor.execute(sql)

            cursor.close()
            connDb.close()
            return True
        except mysql.connector.Error as err:
            print(Msg.createTableFail, err)
            return False
