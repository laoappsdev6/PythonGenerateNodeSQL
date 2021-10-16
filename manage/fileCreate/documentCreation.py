from model.name import Name


class DocumentCreation:

    @staticmethod
    def create(className: str, dataFunction: dict, propertyDetail: dict) -> str:
        fileName = className + ".document.json"

        myAllFunction = DocumentCreation.createAllFunction(className, dataFunction, propertyDetail)

        myController = """
{""" + f"\"{className}\"" + """:[
""" + f"""
{myAllFunction}
""" + """
]}
"""
        return fileName, myController,

    @staticmethod
    def createAllFunction(className: str, dataFunction: dict, propertyDetail: dict) -> str:
        myMange = dataFunction[Name.manage]
        myList = dataFunction[Name.list]

        functionManage = DocumentCreation.createManage(className, myMange, propertyDetail)
        functionList = DocumentCreation.createList(className, myList)
        allFunction = functionManage + "," + functionList

        return allFunction

    @staticmethod
    def createManage(className: str, dataManage: dict, propertyDetail: dict) -> str:
        manageKey = dataManage.keys()
        myFunctionResult = ""

        for manage in manageKey:
            functionDetail = dataManage[manage]
            mySelf = functionDetail[Name.self]

            myFormat = ""
            propertyKey = propertyDetail.keys()
            for prop in propertyKey:
                dataType = propertyDetail[prop]
                typeSplit = dataType[0:3]
                if mySelf == Name.insert:
                    if prop != "id":
                        if typeSplit == "int":
                            myFormat += "\"" + f"{prop}" + "\":1,\n"
                        else:
                            myFormat += "\"" + f"{prop}" + "\":\"data\",\n"
                elif mySelf == Name.delete:
                    if prop == "id":
                        myFormat += "\"" + f"{prop}" + "\":1,\n"
                else:
                    if typeSplit == "int":
                        myFormat += "\"" + f"{prop}" + "\":1,\n"
                    else:
                        myFormat += "\"" + f"{prop}" + "\":\"data\",\n"

            myObject = """
            {
                "object":\"""" + f"{className}" + """\",
                "method":\"""" + f"{manage}" + """\",
                "data":{""" + f"{myFormat[0: len(myFormat) - 2]}" + """},
                "token":"YOUR_TOKEN"
            }
            """

            myFunctionResult += myObject + ","

        return myFunctionResult[0:len(myFunctionResult) - 2]

    @staticmethod
    def createList(className: str, dataList: dict) -> str:
        listKey = dataList.keys()
        myFunctionResult = ""

        for myList in listKey:
            functionDetail = dataList[myList]
            mySelf = functionDetail[Name.self]

            myFormat = ""
            if mySelf == Name.listOne:
                myFormat += '"id":1'
            elif mySelf == Name.listAll:
                myFormat += ""
            else:
                myFormat += """ 
                        "page":1,
                        "limit":10,
                        "keyword":""
                    """

            myObject = """
                   {
                       "object":\"""" + f"{className}" + """\",
                       "method":\"""" + f"{myList}" + """\",
                       "data":{""" + f"{myFormat}" + """},
                       "token":"YOUR_TOKEN"
                   }
                   """

            myFunctionResult += myObject + ","

        return myFunctionResult[0:len(myFunctionResult) - 2]
