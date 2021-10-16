import { ELoginMethod } from "../services/method";
import { Request } from '../servers/Request'
import { Response } from '../servers/Response'
import { EMsg, EStatus } from "../services/message";
import { Service } from "../services/services";
import { LoginModel } from "../models/login.model";
import { LoginController } from "../controllers/authorize.controller";

export class LoginApi {

    public static checkMethod(obj: Request): Promise<Response> {
        return new Promise<Response>((resolve, reject) => {

            if (Object.keys(obj.data).length === 0) resolve(Service.getRes([], EMsg.objEmpty, EStatus.fail));

            const loginModel = new LoginModel(obj.data);

            switch (obj.method) {
                case ELoginMethod.login:
                    const validateAdd = loginModel.validateAll();
                    validateAdd == "true" ? resolve(LoginController.login(loginModel)) : resolve(Service.getRes([], validateAdd, EStatus.fail))
                    break;
                default:
                    resolve(Service.getRes([], EMsg.methodNotFound, EStatus.fail))
                    break;
            }
        })
    }
}