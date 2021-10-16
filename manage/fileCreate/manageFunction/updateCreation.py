from model.name import Name


class UpdateCreation:

    @staticmethod
    def functionUpdate(className: str, functionName: str, myOption: str, propertyDetail: dict) -> str:
        isAllColumn = myOption[Name.isAllColumn]
        modelClass = className.capitalize() + "Model"
        isEqual = myOption[Name.where][Name.isEqual]
        notEqual = myOption[Name.where][Name.notEqual]

        if isAllColumn:
            myFunctionDetail = UpdateCreation.isAllColumn(isEqual, notEqual, className, myOption, propertyDetail)
        else:
            myFunctionDetail = UpdateCreation.notAllColumn(isEqual, notEqual, className, myOption, propertyDetail)

        myAddFunction = """
    public static """ + f"""{functionName}""" + """(data: """ + f"""{modelClass}""" + """): Promise<Response> {
        return new Promise<Response>((resolve, reject) => {
    """ + f"""{myFunctionDetail}""" + """
        })
    }
            """
        return myAddFunction

    @staticmethod
    def isAllColumn(isEqual: list, notEqual: list, className: dict, myOption: dict, propertyDetail: dict) -> str:
        tableName = className
        isAlready = myOption[Name.isAlready]
        propertyKey = propertyDetail.keys()
        propertyList = list(propertyKey)

        if not isAlready:
            updateColumn = ""
            whereColumn = ""

            if isEqual:
                for index in isEqual:
                    myColumn = propertyList[index]
                    whereColumn = whereColumn + myColumn + "='${data." + myColumn + "}' and "

            if notEqual:
                for index in notEqual:
                    myColumn = propertyList[index]
                    whereColumn = whereColumn + myColumn + "!='${data." + myColumn + "}' and "

            for column in propertyKey:
                if column != "id":
                    updateColumn = updateColumn + column + "='${data." + column + "}',"

            updateFormat = updateColumn[0:len(updateColumn) - 1]
            whereFormat = whereColumn[0:len(whereColumn) - 4]

            updateAllColumn = """
                const sql = `update """ + f"""{tableName}""" + """ set """ + f"""{updateFormat}""" + """ 
                            where """ + f"""{whereFormat}""" + """`;
                
                Databases.update(sql).then(result => {
                resolve(result)
                }); 
                """
        else:
            alreadyIndex = myOption[Name.alreadyExitKey]
            alreadyName = list(propertyDetail.keys())[alreadyIndex]
            updateColumn = ""
            whereColumn = ""

            if isEqual:
                for index in isEqual:
                    myColumn = propertyList[index]
                    whereColumn = whereColumn + myColumn + "='${data." + myColumn + "}' and "

            if notEqual:
                for index in notEqual:
                    myColumn = propertyList[index]
                    whereColumn = whereColumn + myColumn + "!='${data." + myColumn + "}' and "

            for column in propertyKey:
                if column != "id":
                    updateColumn = updateColumn + column + "='${data." + column + "}',"

            updateFormat = updateColumn[0:len(updateColumn) - 1]
            whereFormat = whereColumn[0:len(whereColumn) - 4]

            updateAllColumn = """
                 const sql""" + f"""{alreadyName.capitalize()}""" + """ = `select * from """ + f"""{tableName}""" + """ where """ + f"""{alreadyName}""" + """='${data.""" + f"""{alreadyName}""" + """}' and and id!='${data.id}'`;
                        ValidateController.alreadyExist(sql""" + f"""{alreadyName.capitalize()}""" + """).then((result) => {

                            if (result) {
                                const msg = already(\"""" + f"""{alreadyName}""" + """\", data.""" + f"""{alreadyName}""" + """);
                                resolve(Service.getRes([], msg, 0));

                            } else {
                                const sql = `update """ + f"""{tableName}""" + """ set """ + f"""{updateFormat}""" + """ 
                                     where """ + f"""{whereFormat}""" + """`;
                
                                Databases.update(sql).then(result => {
                                resolve(result)
                                }); 
                            }
                })"""

        return updateAllColumn

    @staticmethod
    def notAllColumn(isEqual: list, notEqual: list, className: str, myOption: dict, propertyDetail: dict) -> str:
        tableName = className
        isAlready = myOption[Name.isAlready]
        propertyKey = propertyDetail.keys()
        propertyList = list(propertyKey)
        columnDetail = myOption[Name.columnDetail]

        if not isAlready:
            updateColumn = ""
            whereColumn = ""

            if isEqual:
                for index in isEqual:
                    myColumn = propertyList[index]
                    whereColumn = whereColumn + myColumn + "='${data." + myColumn + "}' and "

            if notEqual:
                for index in notEqual:
                    myColumn = propertyList[index]
                    whereColumn = whereColumn + myColumn + "!='${data." + myColumn + "}' and "

            for index in columnDetail:
                column = propertyList[index]
                updateColumn = updateColumn + column + "='${data." + column + "}',"

            updateFormat = updateColumn[0:len(updateColumn) - 1]
            whereFormat = whereColumn[0:len(whereColumn) - 4]

            updateManyColumn = """
                        const sql = `update """ + f"""{tableName}""" + """ set """ + f"""{updateFormat}""" + """ 
                                    where """ + f"""{whereFormat}""" + """`;

                        Databases.update(sql).then(result => {
                        resolve(result)
                        }); 
                        """
        else:
            alreadyIndex = myOption[Name.alreadyExitKey]
            alreadyName = list(propertyDetail.keys())[alreadyIndex]
            updateColumn = ""
            whereColumn = ""

            if isEqual:
                for index in isEqual:
                    myColumn = propertyList[index]
                    whereColumn = whereColumn + myColumn + "='${data." + myColumn + "}' and "

            if notEqual:
                for index in notEqual:
                    myColumn = propertyList[index]
                    whereColumn = whereColumn + myColumn + "!='${data." + myColumn + "}' and "

            for index in columnDetail:
                column = propertyList[index]
                updateColumn = updateColumn + column + "='${data." + column + "}',"

            updateFormat = updateColumn[0:len(updateColumn) - 1]
            whereFormat = whereColumn[0:len(whereColumn) - 4]

            updateManyColumn = """
                         const sql""" + f"""{alreadyName.capitalize()}""" + """ = `select * from """ + f"""{tableName}""" + """ where """ + f"""{alreadyName}""" + """='${data.""" + f"""{alreadyName}""" + """}' and and id!='${data.id}'`;
                                ValidateController.alreadyExist(sql""" + f"""{alreadyName.capitalize()}""" + """).then((result) => {

                                    if (result) {
                                        const msg = already(\"""" + f"""{alreadyName}""" + """\", data.""" + f"""{alreadyName}""" + """);
                                        resolve(Service.getRes([], msg, 0));

                                    } else {
                                        const sql = `update """ + f"""{tableName}""" + """ set """ + f"""{updateFormat}""" + """ 
                                             where """ + f"""{whereFormat}""" + """`;

                                        Databases.update(sql).then(result => {
                                        resolve(result)
                                        }); 
                                    }
                        })"""
        return updateManyColumn
