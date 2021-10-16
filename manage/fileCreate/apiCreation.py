from model.name import Name


class ApiCreation:

    @staticmethod
    def create(className: str, allFunction: dict) -> str:
        fileName = className + ".api.ts"
        myClass = className.capitalize() + "Api"

        functionDetail, listAll = ApiCreation.createDetail(className, allFunction)

        myApi = """
import { """ + f"""{className.capitalize()}""" + """Controller } from "../controllers/""" + f"""{className}""" + """.controller";
import { E""" + f"""{className.capitalize()}""" + """Method } from "../services/method";
import { Request } from '../servers/Request'
import { Response } from '../servers/Response'
import { """ + f"""{className.capitalize()}""" + """Model } from "../models/""" + f"""{className}""" + """.model";
import { EMsg, EStatus } from "../services/message";
import { Service } from "../services/services";

export class """ + f"""{myClass}""" + """ {

    public static checkMethod(obj: Request): Promise<Response> {
        return new Promise<Response>((resolve, reject) => {

            if (Object.keys(obj.data).length === 0 && obj.method !== E""" + f"""{className.capitalize()}""" + """Method.""" + f"""{listAll}""" + """) {
                resolve(Service.getRes([], EMsg.objEmpty, EStatus.fail));

            } else {

                const """ + f"""{className}""" + """Model = new """ + f"""{className.capitalize()}""" + """Model(obj.data);

                switch (obj.method) {
                    """ + f"""{functionDetail}""" + """
                    default:
                        resolve(Service.getRes([], EMsg.methodNotFound, EStatus.fail))
                        break;
                }
            }
        })
    }
}
        """
        return fileName, myApi

    @staticmethod
    def createDetail(className: str, allFunction: dict) -> str:
        manageMethod = allFunction[Name.manage]
        listMethod = allFunction[Name.list]
        manageKey = manageMethod.keys()
        listKey = listMethod.keys()
        # allKey = manageKey | listKey

        manageDetail = ApiCreation.manageFunction(className, manageKey, allFunction)
        listDetail, listAll = ApiCreation.listFunction(className, listKey, allFunction)

        return manageDetail + listDetail, listAll

    @staticmethod
    def manageFunction(className: str, manageKey: dict, allFunction: str) -> str:
        manageDetail = ""
        for manage in manageKey:
            myValidate = allFunction[Name.manage][manage][Name.option][Name.validate]
            mySelf = allFunction[Name.manage][manage][Name.self]

            if myValidate:

                if mySelf == Name.update:
                    isSelf = "false,true"
                elif mySelf == Name.delete:
                    isSelf = "false,false,true"
                else:
                    isSelf = ""

                functionValidate = """
                    case E""" + f"""{className.capitalize()}""" + """Method.""" + f"""{manage}""" + """:
                        const validate""" + f"""{manage.capitalize()}""" + """ = """ + f"""{className}""" + """Model.validateAll(""" + f"""{isSelf}""" + """);
                        validate""" + f"""{manage.capitalize()}""" + """ == "true" ? resolve(""" + f"""{className.capitalize()}""" + """Controller.""" + f"""{manage}""" + """(""" + f"""{className}""" + """Model)) : resolve(Service.getRes([], validate""" + f"""{manage.capitalize()}""" + """, EStatus.fail))
                        break
                """
                manageDetail = manageDetail + functionValidate
            else:
                functionNotValidate = """
                    case E""" + f"""{className.capitalize()}""" + """Method.""" + f"""{manage}""" + """:
                        resolve(""" + f"""{className.capitalize()}""" + """Controller.""" + f"""{manage}""" + """(""" + f"""{className}""" + """Model))
                        break;
                """
                manageDetail = manageDetail + functionNotValidate

        return manageDetail

    @staticmethod
    def listFunction(className: str, manageKey: dict, allFunction: str) -> str:
        listDetail = ""
        listAll = ""
        for myList in manageKey:
            mySelf = allFunction[Name.list][myList][Name.self]

            if mySelf == Name.listAll:
                listAll = myList

            functionNotValidate = """
                    case E""" + f"""{className.capitalize()}""" + """Method.""" + f"""{myList}""" + """:
                        resolve(""" + f"""{className.capitalize()}""" + """Controller.""" + f"""{myList}""" + """(""" + f"""{className}""" + """Model))
                        break;
                    """
            listDetail = listDetail + functionNotValidate

        return listDetail, listAll
