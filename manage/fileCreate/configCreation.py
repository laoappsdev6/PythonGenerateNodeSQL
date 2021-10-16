class ConfigCreation:

    @staticmethod
    def create(databaseName: str) -> str:
        fileName = "config.ts"

        myBase = """
export enum EServer {
    allHost = "0.0.0.0",
    httpPort = 4500,
    tcpPort = 4600,
    socketPort = 4700
}

export enum EDB {
    dbhost = 'localhost',
    dbname = '"""+f"{databaseName}"+"""',
    dbuser = 'root',
    dbpass = '',
    dbdialect = 'mysql',
    dbport = '',
    timezone = '+07:00'
}
            """
        return fileName, myBase
