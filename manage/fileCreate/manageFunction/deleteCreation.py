from model.name import Name


class DeleteCreation:

    @staticmethod
    def functionDelete(className: str, functionName: str, myOption: str, propertyDetail: dict) -> str:
        modelClass = className.capitalize() + "Model"
        isEqual = myOption[Name.where][Name.isEqual]
        notEqual = myOption[Name.where][Name.notEqual]

        myFunctionDetail = DeleteCreation.createDetail(className, isEqual, notEqual, propertyDetail)

        myAddFunction = """
    public static """ + f"""{functionName}""" + """(data: """ + f"""{modelClass}""" + """): Promise<Response> {
        return new Promise<Response>((resolve, reject) => {
    """ + f"""{myFunctionDetail}""" + """
        })
    }
            """
        return myAddFunction

    @staticmethod
    def createDetail(className: str, isEqual: list, notEqual: list, propertyDetail: dict) -> str:
        tableName = className
        propertyKey = propertyDetail.keys()
        propertyList = list(propertyKey)

        whereColumn = ""
        if isEqual:
            for index in isEqual:
                myColumn = propertyList[index]
                whereColumn = whereColumn + myColumn + "='${data." + myColumn + "}' and "

        if notEqual:
            for index in notEqual:
                myColumn = propertyList[index]
                whereColumn = whereColumn + myColumn + "!='${data." + myColumn + "}' and "

        whereFormat = whereColumn[0:len(whereColumn) - 4]

        deleteAllColumn = """
                    const sql = `delete from """ + f"""{tableName}""" + """ where """ + f"""{whereFormat}""" + """`;
                    Databases.delete(sql).then(result => {
                        resolve(result)
                    });
                     """

        return deleteAllColumn
