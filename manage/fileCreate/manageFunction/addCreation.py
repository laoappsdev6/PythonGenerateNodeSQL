from model.name import Name


class AddCreation:

    @staticmethod
    def functionAdd(className: str, functionName: str, myOption: str, propertyDetail: dict) -> str:
        isAllColumn = myOption[Name.isAllColumn]
        modelClass = className.capitalize() + "Model"

        if isAllColumn:
            myFunctionDetail = AddCreation.isAllColumn(className, myOption, propertyDetail)
        else:
            myFunctionDetail = AddCreation.notAllColumn(className, myOption, propertyDetail)

        myAddFunction = """
    public static """ + f"""{functionName}""" + """(data: """ + f"""{modelClass}""" + """): Promise<Response> {
        return new Promise<Response>((resolve, reject) => {
    """ + f"""{myFunctionDetail}""" + """
        })
    }
            """
        return myAddFunction

    @staticmethod
    def isAllColumn(className: str, myOption: dict, propertyDetail: dict) -> str:
        tableName = className
        isAlready = myOption[Name.isAlready]
        propertyKey = propertyDetail.keys()

        if not isAlready:
            insertKeys = ""
            insertValues = ""
            for column in propertyKey:
                if column != "id":
                    insertKeys = insertKeys + column + ","
                    insertValues = insertValues + "'${data." + column + "}',"

            keysFormat = insertKeys[0:len(insertKeys) - 1]
            valuesFormat = insertValues[0:len(insertValues) - 1]

            addAllColumn = """
                         const sql = `insert into """ + f"""{tableName}""" + """ (""" + f"""{keysFormat}""" + """)
                                  values (""" + f"""{valuesFormat}""" + """)`;
                                  
                         Databases.insert(sql).then(result => {
                             resolve(result)
                         }); 
                         """
        else:
            alreadyIndex = myOption[Name.alreadyExitKey]
            alreadyName = list(propertyDetail.keys())[alreadyIndex]
            insertKeys = ""
            insertValues = ""
            for column in propertyKey:
                if column != "id":
                    insertKeys = insertKeys + column + ","
                    insertValues = insertValues + "'${data." + column + "}',"

            keysFormat = insertKeys[0:len(insertKeys) - 1]
            valuesFormat = insertValues[0:len(insertValues) - 1]

            addAllColumn = """
                 const sql""" + f"""{alreadyName.capitalize()}""" + """ = `select * from """ + f"""{tableName}""" + """ where """ + f"""{alreadyName}""" + """='${data.""" + f"""{alreadyName}""" + """}'`;
                        ValidateController.alreadyExist(sql""" + f"""{alreadyName.capitalize()}""" + """).then((result) => {

                            if (result) {
                                const msg = already(\"""" + f"""{alreadyName}""" + """\", data.""" + f"""{alreadyName}""" + """);
                                resolve(Service.getRes([], msg, 0));

                            } else {
                                const sql = `insert into """ + f"""{tableName}""" + """ (""" + f"""{keysFormat}""" + """)
                                         values (""" + f"""{valuesFormat}""" + """)`;
                                         
                                Databases.insert(sql).then(result => {
                                    resolve(result)
                                });
                            }
                })"""
        return addAllColumn

    @staticmethod
    def notAllColumn(className: str, myOption: dict, propertyDetail: dict) -> str:
        tableName = className
        propertyKey = list(propertyDetail.keys())
        isAlready = myOption[Name.isAlready]
        columnDetail = myOption[Name.columnDetail]

        if not isAlready:
            insertKeys = ""
            insertValues = ""
            for index in columnDetail:
                insertKeys = insertKeys + propertyKey[index] + ","
                insertValues = insertValues + "'${data." + propertyKey[index] + "}',"

            keysFormat = insertKeys[0:len(insertKeys) - 1]
            valuesFormat = insertValues[0:len(insertValues) - 1]

            addAllColumn = """
                                const sql = `insert into """ + f"""{tableName}""" + """ (""" + f"""{keysFormat}""" + """)
                                         values (""" + f"""{valuesFormat}""" + """)`;
                                         
                                Databases.insert(sql).then(result => {
                                    resolve(result)
                                }); 
                                """
        else:
            alreadyIndex = myOption[Name.alreadyExitKey]
            alreadyName = list(propertyDetail.keys())[alreadyIndex]
            insertKeys = ""
            insertValues = ""
            for index in columnDetail:
                insertKeys = insertKeys + propertyKey[index] + ","
                insertValues = insertValues + "'${data." + propertyKey[index] + "}',"

            keysFormat = insertKeys[0:len(insertKeys) - 1]
            valuesFormat = insertValues[0:len(insertValues) - 1]

            addAllColumn = """
                        const sql""" + f"""{alreadyName.capitalize()}""" + """ = `select * from """ + f"""{tableName}""" + """ where """ + f"""{alreadyName}""" + """='${data.""" + f"""{alreadyName}""" + """}'`;
                               ValidateController.alreadyExist(sql""" + f"""{alreadyName.capitalize()}""" + """).then((result) => {

                                   if (result) {
                                       const msg = already(\"""" + f"""{alreadyName}""" + """\", data.""" + f"""{alreadyName}""" + """);
                                       resolve(Service.getRes([], msg, 0));

                                   } else {
                                       const sql = `insert into """ + f"""{tableName}""" + """ (""" + f"""{keysFormat}""" + """)
                                                values (""" + f"""{valuesFormat}""" + """)`;
                                                
                                       Databases.insert(sql).then(result => {
                                           resolve(result)
                                       });
                                   }
                       })"""

        return addAllColumn
