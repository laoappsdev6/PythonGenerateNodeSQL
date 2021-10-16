from model.name import Name


class ListOneCreation:

    @staticmethod
    def functionListOne(className: str, functionName: str, myOption: str, propertyDetail: dict, allTable: dict) -> str:
        modelClass = className.capitalize() + "Model"

        myFunctionDetail = ListOneCreation.createFunction(className, myOption, propertyDetail, allTable)

        myListOneFunction = """
    public static """ + f"""{functionName}""" + """(data: """ + f"""{modelClass}""" + """): Promise<Response> {
        return new Promise<Response>((resolve, reject) => {
        """ + f"""{myFunctionDetail}""" + """
        })
    }
                   """
        return myListOneFunction

    @staticmethod
    def createFunction(className: str, myOption: dict, propertyDetail: dict, allTable: dict) -> str:

        isJoin = myOption[Name.isJoin]
        tableName = className
        propertyKey = propertyDetail.keys()

        if isJoin:
            myListOne = ListOneCreation.isJoinFunction(tableName, myOption, propertyKey, allTable)
        else:
            myListOne = ListOneCreation.notJoinFunction(tableName, myOption, propertyKey)

        return myListOne

    @staticmethod
    def isJoinFunction(tableName: str, myOption: dict, propertyKey: dict, allTable: dict) -> str:

        listTableWhere = myOption[Name.where]
        whereDetailKey = listTableWhere.keys()
        listTableJoin = myOption[Name.joinDetail]
        listTableJoinKey = listTableJoin.keys()

        myColumn = ""
        asTable = tableName[0:2]
        myFrom = "from " + tableName + " as " + asTable
        myWhere = "where "

        # loop for original table
        for column in propertyKey:
            if column == "id":
                myColumn += asTable + ".id as " + tableName + "Id,"
            else:
                myColumn += asTable + "." + column + ","

        myColumn += "\n\t\t\t\t\t\t\t\t\t"
        myFrom += "\n"

        # loop for table join
        for tableNames in listTableJoinKey:
            joinToTableName = listTableJoin[tableNames][Name.joinTo]
            foreignKeyIndex = listTableJoin[tableNames][Name.foreignKey]
            foreignKeyName = list(allTable[joinToTableName][Name.field].keys())[foreignKeyIndex]
            fieldOfTableJoin = allTable[tableNames][Name.field].keys()
            titleTable = tableNames[0:2]
            titleJoinTo = joinToTableName[0:2]

            # loop for column join
            for columnIndex in fieldOfTableJoin:
                if columnIndex == "id":
                    myColumn += titleTable + ".id as " + tableNames + "Id,"
                else:
                    myColumn += titleTable + "." + columnIndex + ","
            myColumn += "\n\t\t\t\t\t\t\t\t\t"

            myFrom += f"\t\t\t\t\t\t\t\t\tINNER JOIN  {tableNames} as {titleTable}  ON {titleJoinTo}.{foreignKeyName} = {titleTable}.id\n"

        # loop for where all table
        for where in whereDetailKey:
            whereIndex = listTableWhere[where]
            whereColumn = list(allTable[where][Name.field].keys())[whereIndex]
            titleTableWhere = where[0:2]

            myWhere += f"{titleTableWhere}.{whereColumn}=" + "'${data." + whereColumn + "}' and "

        columnFormat = myColumn[0:len(myColumn) - 11]
        whereFormat = myWhere[0:len(myWhere) - 5]

        listOneQuery = """
                       const sql = `select """ + f"""{columnFormat}""" + """ 
                                            """ + f"""{myFrom}""" + """ 
                                            """ + f"""{whereFormat}""" + """ `;
                       Databases.selectOne(sql).then(result => {
                           resolve(result)
                       }); 
                                   """

        return listOneQuery

    @staticmethod
    def notJoinFunction(tableName: str, myOption: dict, propertyKey: dict) -> str:
        whereIndex = myOption[Name.where]
        myWhereColumn = list(propertyKey)[whereIndex]
        listOneQuery = """
            const sql = `select * from """ + f"""{tableName}""" + """ where """ + f"""{myWhereColumn}""" + """ = ${data.""" + f"""{myWhereColumn}""" + """}`;
            Databases.selectOne(sql).then(result => {
                resolve(result)
            });
                                       """

        return listOneQuery
