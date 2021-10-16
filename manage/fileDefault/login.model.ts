import { isEmpty } from "./validate.model";

export class LoginModel {
    username: string;
    password: string;


    constructor(data: Object) {
        Object.assign(this, data);
    }

    public validateAll(): string {

        if (!this.username) {
            return isEmpty("username")
        }
        if (!this.password) {
            return isEmpty("password")
        }
        return "true";
    }
}
