from model.name import Name


class ListPageCreation:

    @staticmethod
    def functionListAll(className: str, functionName: str, myOption: str, propertyDetail: dict, allTable: dict) -> str:
        modelClass = className.capitalize() + "Model"

        myFunctionDetail = ListPageCreation.createFunction(className, myOption, propertyDetail, allTable)

        myListOneFunction = """
    public static """ + f"""{functionName}""" + """(data: """ + f"""{modelClass}""" + """): Promise<Response> {
        return new Promise<Response>((resolve, reject) => {
            const page = data.page ? data.page : 1;
            const limit = data.limit ? data.limit : 10;
            const offset = (page - 1) * limit;
            
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
            myListOne = ListPageCreation.isJoinFunction(tableName, myOption, propertyKey, allTable)
        else:
            myListOne = ListPageCreation.notJoinFunction(tableName, myOption, propertyKey)

        return myListOne

    @staticmethod
    def isJoinFunction(tableName: str, myOption: dict, propertyKey: dict, allTable: dict):


        listTableJoin = myOption[Name.joinDetail]
        listTableJoinKey = listTableJoin.keys()
        isWhere = myOption[Name.isWhere]

        myColumn = ""
        asTable = tableName[0:2]
        myFrom = "from " + tableName + " as " + asTable
        myWhere = ""

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
        if isWhere:
            listTableWhere = myOption[Name.where]
            whereDetailKey = listTableWhere.keys()
            myWhere = "where "
            searchKeyWordIndex = myOption[Name.searchKey]
            for where in whereDetailKey:
                whereIndex = listTableWhere[where]
                whereColumn = list(allTable[where][Name.field].keys())[whereIndex]
                titleTableWhere = where[0:2]

                myWhere += f"{titleTableWhere}.{whereColumn}=" + "'${data." + whereColumn + "}' and "
            if searchKeyWordIndex > -1:
                searchColumnName = list(propertyKey)[searchKeyWordIndex]
                myWhere += """( """+f"""{searchColumnName}"""+""" like '%${data."""+f"""{searchColumnName}"""+"""}%') and """

        columnFormat = myColumn[0:len(myColumn) - 11]
        whereFormat = myWhere[0:len(myWhere) - 5]

        listAllQuery = """
                        const sqlCount = `select count(*) as count """ + f"""{myFrom}""" + """ 
                                            """ + f"""{whereFormat}""" + """  `;
                                        
                        const sqlPage = `select  """ + f"""{columnFormat}""" + """ 
                                        """ + f"""{myFrom}""" + """ 
                                        """ + f"""{whereFormat}""" + """ 
                                        order by """+f"""{asTable}"""+""".id desc limit ${limit} offset ${offset} `;
                        
                        Databases.selectPage(sqlCount, sqlPage).then(result => {
                        resolve(result)
                        });
                                   """
        return listAllQuery

    @staticmethod
    def notJoinFunction(tableName: str, myOption: dict, propertyKey: dict) -> str:
        isWhere = myOption[Name.isWhere]
        searchKeyWordIndex = myOption[Name.searchKey]
        myWhere = ""

        if isWhere:
            whereColumnIndex = myOption[Name.where]
            whereColumnName = list(propertyKey)[whereColumnIndex]
            if searchKeyWordIndex > -1:
                searchColumnName = list(propertyKey)[searchKeyWordIndex]
                myWhere = """where """+f"""{whereColumnName}"""+"""='${data."""+f"""{whereColumnName}"""+"""}' 
                            and ("""+f"""{searchColumnName}"""+""" like '%${data."""+f"""{searchColumnName}"""+"""}%') """
            else:
                myWhere = """where """+f"""{whereColumnName}"""+"""='${data."""+f"""{whereColumnName}"""+"""}' """

        listAllQuery = """
            const sqlCount = "select count(*) as count from """+f"""{tableName}"""+""" ";
            const sqlPage = `select * from """+f"""{tableName} {myWhere}"""+""" order by id desc limit ${limit} offset ${offset} `;

            Databases.selectPage(sqlCount, sqlPage).then(result => {
                resolve(result)
            });
                                       """
        return listAllQuery
