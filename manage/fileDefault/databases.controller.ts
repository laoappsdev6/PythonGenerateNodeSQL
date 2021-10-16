import mysql from 'mysql';
import { EDB } from '../config/config';
import { Service } from '../services/services';
import { EMsg, EStatus } from '../services/message';
import { Response } from '../servers/Response';

export class Databases {
    public static connection(): Promise<mysql.Connection> {
        return new Promise<mysql.Connection>(async (resolve, reject) => {
            try {
                const params = {
                    user: EDB.dbuser,
                    password: EDB.dbpass,
                    host: EDB.dbhost,
                    database: EDB.dbname
                };

                const connection = mysql.createConnection(params);

                connection.connect((error) => {
                    if (error) {
                        reject(error);
                        return;
                    }
                    resolve(connection);
                });
            } catch (error) {
                reject(error);
            }
        })
    }

    public static query(connection: mysql.Connection, sql: string): Promise<Array<any>> {
        return new Promise<Array<any>>((resolve, reject) => {
            try {
                connection.query(sql, connection, (error, result) => {
                    if (error) {
                        reject(error);
                        return;
                    }
                    resolve(result);
                });
            } catch (error) {
                reject(error);
            }
        })
    }
    public static insert(sql: string): Promise<Response> {
        return new Promise<Response>((resolve, reject) => {
            try {
                Databases.connection().then((connection) => {
                    Databases.query(connection, sql).then((result) => {
                        resolve(Service.getRes(result, EMsg.addSuccess, EStatus.success));
                        connection.destroy();
                    })
                })
            } catch (error) {
                resolve(Service.getRes([error], EMsg.addFail, EStatus.fail));
            }
        })
    }
    public static update(sql: string): Promise<Response> {
        return new Promise<Response>((resolve, reject) => {
            try {
                Databases.connection().then((connection) => {
                    Databases.query(connection, sql).then((result) => {
                        resolve(Service.getRes(result, EMsg.updateSuccess, EStatus.success));
                        connection.destroy();
                    })
                })
            } catch (error) {
                resolve(Service.getRes([error], EMsg.updateFail, EStatus.fail));
            }
        })
    }
    public static delete(sql: string): Promise<Response> {
        return new Promise<Response>((resolve, reject) => {
            try {
                Databases.connection().then((connection) => {
                    Databases.query(connection, sql).then((result) => {
                        resolve(Service.getRes(result, EMsg.deleteSuccess, EStatus.success));
                        connection.destroy();
                    })
                })
            } catch (error) {
                resolve(Service.getRes([error], EMsg.deleteFail, EStatus.fail));
            }
        })
    }

    public static selectOne(sql: string): Promise<Response> {
        return new Promise<Response>((resolve, reject) => {
            try {
                Databases.connection().then((connection) => {
                    Databases.query(connection, sql).then((result) => {
                        resolve(Service.getRes(result, EMsg.listOne, EStatus.success));
                        connection.destroy();
                    })
                })
            } catch (error) {
                resolve(Service.getRes([error], EMsg.listOne, EStatus.fail));
            }
        })
    }
    public static selectPage(sqlCount: string, sqlPage: string): Promise<Response> {
        return new Promise<Response>((resolve, reject) => {
            try {
                Databases.connection().then((connection) => {
                    Databases.query(connection, sqlCount).then((count) => {
                        const num = count[0].count
                        if (num > 0) {
                            Databases.query(connection, sqlPage).then((row) => {
                                const data = {
                                    count: num,
                                    rows: row
                                }
                                resolve(Service.getRes(data, EMsg.listPage, EStatus.success));
                                connection.destroy();
                            })
                        } else {
                            resolve(Service.getRes([], EMsg.listPage, EStatus.fail));
                        }
                    })
                })
            } catch (error) {
                resolve(Service.getRes([error], EMsg.listPage, EStatus.fail));
            }
        })
    }

    public static selectAll(sql: string): Promise<Response> {
        return new Promise<Response>(async (resolve, reject) => {
            try {
                await Databases.connection().then(async (connection) => {
                    await Databases.query(connection, sql).then((result) => {
                        resolve(Service.getRes(result, EMsg.listAll, EStatus.success));
                        connection.destroy();
                    })
                })
            } catch (error) {
                resolve(Service.getRes([error], EMsg.listAll, EStatus.fail));
            }
        })
    }
}