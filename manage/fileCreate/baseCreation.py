class BaseCreation:

    @staticmethod
    def create(apiList: dict) -> str:
        fileName = "base.api.ts"

        apiImport, apiObject = BaseCreation.createDetail(apiList)

        myBase = """
import { Request } from '../servers/Request'
import { Response } from '../servers/Response'
import { EMsg, EStatus } from '../services/message'
import { EObject } from '../services/object'
import { Service } from '../services/services'
import { LoginApi } from './login.api'
""" + f"""{apiImport}""" + """


export class BaseApi {

    public static checkObject(obj: Request): Promise<Response> {
        return new Promise<Response>((resolve, reject) => {

            if (!Service.validateToken(obj.token) && obj.object !== EObject.login) {
                resolve(Service.getRes([], EMsg.noAuthorize, EStatus.fail))
            } else {

                switch (obj.object) {
                    case EObject.login:
                        resolve(LoginApi.checkMethod(obj))
                        break;
                """ + f"""{apiObject}""" + """
                    default:
                        resolve(Service.getRes([], EMsg.objectNotFound, EStatus.fail))
                        break;
                }
            }
        })
    }
}      
            """
        return fileName, myBase

    @staticmethod
    def createDetail(apiList: dict) -> str:
        apiImport = ""
        apiObject = ""
        for api in apiList:
            importFormat = "import { " + f"{api.capitalize()}" + "Api } from './" + f"{api}" + ".api'"
            apiImport = apiImport + importFormat + "\n"

            objectFormat = """
                case EObject.""" + f"""{api}""" + """:
                    resolve(""" + f"""{api.capitalize()}""" + """Api.checkMethod(obj))
                    break;"""
            apiObject = apiObject + objectFormat + "\n"

        return apiImport, apiObject
