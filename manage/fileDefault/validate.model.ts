import { EMsg } from "../services/message";

export function isEmpty(key: string): string {
    return key + EMsg.empty
}

export function isNumber(key: string): string {
    return key + EMsg.number
}

export function already(key: string, value: string): string {
    return key + " : " + value + EMsg.already
}

export function notExist(key: string, value: string): string {
    return key + " : " + value + EMsg.exists
}