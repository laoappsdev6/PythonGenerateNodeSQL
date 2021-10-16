import * as jwt from 'jsonwebtoken';
import date from 'date-and-time';
import * as uuid from 'uuid';
import { Response } from '../servers/Response'

export class Service {

    public static getRes(data: any, message: string, status: number): Response {
        const respon = new Response();
        respon.status = status;
        respon.message = message;
        respon.data = data;
        return respon;
    }

    static jwtEncode(data: Array<any>): string {
        try {
            return jwt.sign({
                data,
            }, Keys.jwtKey, { expiresIn: '10000000000H' });
        } catch (error) {
            console.log(error);
            return null;
        }
    }

    static validateToken(jwtEncode: string): boolean {
        if (jwtEncode) {
            try {
                jwt.verify(jwtEncode, Keys.jwtKey);
                return true;
            } catch (error) {
                return false;
            }
        } else {
            return false;
        }
    }

    public static genUUID(): string {
        return uuid.v1();
    }

    public static nDate(): string {
        const dd = new Date();
        return date.format(dd, 'YYYY-MM-DD HH:mm:ss');
    }

    public static clone(data: any) {
        return JSON.parse(JSON.stringify(data))
    }

    public static copyObject(a: any, b: any) {
        for (const key in a) {
            if (Object.prototype.hasOwnProperty.call(a, key)) {
                b[key] = a[key];
            }
        }
    }
}

enum Keys {
    jwtKey = 'Dx4YsbptOGuHmL94qdC2YAPqsUFpzJkc',
    superadminkey = '9F58A83B7628211D6E739976A3E3A'
}