import { Service } from '../services/services';
import { Databases } from './databases.controller';
import { LoginModel } from '../models/login.model';
import { EMsg, EStatus } from '../services/message';
import { Response } from '../servers/Response';
export class LoginController {
    public static login(data: LoginModel): Promise<Response> {
        return new Promise<Response>((resolve, reject) => {
            try {

                const sql = `select * from users where username='${data.username}' and password='${data.password}'`;

                Databases.connection().then((connection) => {
                    Databases.query(connection, sql).then((result) => {
                        if (result[0]) {
                            const users = Service.clone(result[0])
                            delete users.password;
                            const token = Service.jwtEncode(users);
                            const data = {
                                user: users,
                                token: token
                            }
                            resolve(Service.getRes(data, EMsg.loginSuccess, EStatus.success))
                            connection.destroy();
                        } else {
                            resolve(Service.getRes([], EMsg.wrongAccount, EStatus.fail));
                            connection.destroy();
                        }
                    })
                })
            } catch (error) {
                resolve(Service.getRes([error], EMsg.loginFail, 0));
            }
        })
    }
}
