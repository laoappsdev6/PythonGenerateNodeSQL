import { Databases } from "./databases.controller";

export class ValidateController {
    public static alreadyExist(sql: string): Promise<boolean> {
        return new Promise<boolean>(async (resolve, reject) => {
            await Databases.connection().then(async (connection) => {
                await Databases.query(connection, sql).then((result) => {
                    if (result[0]) {
                        resolve(true)
                        connection.destroy();
                    } else {
                        resolve(false);
                        connection.destroy();
                    }
                })
            })
        })
    }
    public static notExist(sql: string): Promise<boolean> {
        return new Promise<boolean>(async (resolve, reject) => {
            await Databases.connection().then(async (connection) => {
                await Databases.query(connection, sql).then((result) => {
                    if (result[0]) {
                        resolve(false)
                        connection.destroy();
                    } else {
                        reject(true);
                        connection.destroy();
                    }
                })
            })
        })
    }
}