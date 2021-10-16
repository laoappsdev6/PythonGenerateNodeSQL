from manage.fileCreate.listFunction.listAllCreation import ListAllCreation
from manage.fileCreate.listFunction.listOneCreation import ListOneCreation
from manage.fileCreate.listFunction.listPageCreation import ListPageCreation
from manage.fileCreate.manageFunction.addCreation import AddCreation
from manage.fileCreate.manageFunction.deleteCreation import DeleteCreation
from manage.fileCreate.manageFunction.updateCreation import UpdateCreation
from model.name import Name


class ControllerCreation:

    @staticmethod
    def create(className: str, dataFunction: dict, propertyDetail: dict, allTable: dict) -> str:
        fileName = className + ".controller.ts"
        myClass = className.capitalize()
        controllerClass = myClass + "Controller"

        myAllFunction = ControllerCreation.createAllFunction(className, dataFunction, propertyDetail, allTable)

        myController = """
import { """ + f"""{myClass}""" + """Model } from '../models/""" + f"""{className}""" + """.model';
import { Service } from '../services/services';
import { Databases } from './databases.controller';
import { ValidateController } from './validate.controller';
import { Response } from '../servers/Response';
import { already } from '../models/validate.model';
""" + f"""
export class {controllerClass} 
""" + """
{
""" + f"""
{myAllFunction}
""" + """
}
"""
        return fileName, myController,

    @staticmethod
    def createAllFunction(className: str, dataFunction: dict, propertyDetail: dict, allTable: dict) -> str:
        myMange = dataFunction[Name.manage]
        myList = dataFunction[Name.list]

        functionManage = ControllerCreation.createManage(className, myMange, propertyDetail)
        functionList = ControllerCreation.createList(className, myList, propertyDetail, allTable)
        allFunction = functionManage + functionList

        return allFunction

    @staticmethod
    def createManage(className: str, dataManage: dict, propertyDetail: dict) -> str:
        manageKey = dataManage.keys()
        myFunctionResult = ""
        for functionName in manageKey:
            functionDetail = dataManage[functionName]
            mySelf = functionDetail[Name.self]
            myOption = functionDetail[Name.option]

            if mySelf == Name.insert:
                addResult = AddCreation.functionAdd(className, functionName, myOption, propertyDetail)
                myFunctionResult += addResult

            elif mySelf == Name.update:
                updateResult = UpdateCreation.functionUpdate(className, functionName, myOption, propertyDetail)
                myFunctionResult += updateResult

            elif mySelf == Name.delete:
                deleteResult = DeleteCreation.functionDelete(className, functionName, myOption, propertyDetail)
                myFunctionResult += deleteResult

        return myFunctionResult

    @staticmethod
    def createList(className: str, dataList: dict, propertyDetail: dict, allTable: dict) -> str:
        listKey = dataList.keys()
        myFunctionResult = ""
        for functionName in listKey:
            functionDetail = dataList[functionName]
            mySelf = functionDetail[Name.self]
            myOption = functionDetail[Name.option]

            if mySelf == Name.listOne:
                listOneResult = ListOneCreation.functionListOne(className, functionName, myOption, propertyDetail, allTable)
                myFunctionResult +=  listOneResult

            elif mySelf == Name.listAll:
                listAllResult = ListAllCreation.functionListAll(className, functionName, myOption, propertyDetail, allTable)
                myFunctionResult += listAllResult

            elif mySelf == Name.listPage:
                listPageResult = ListPageCreation.functionListAll(className, functionName, myOption, propertyDetail, allTable)
                myFunctionResult += listPageResult

        return myFunctionResult
