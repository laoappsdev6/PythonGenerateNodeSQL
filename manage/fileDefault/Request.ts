export class Request {
    object: string;
    method: string;
    data: Object;
    token: string;

    constructor(request: Object) {
        Object.assign(this, request);
    }
}