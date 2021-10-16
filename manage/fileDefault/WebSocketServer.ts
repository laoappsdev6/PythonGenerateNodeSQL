import express from 'express';
import http from 'http';
import WebSocket from 'ws';
import { BaseApi } from '../api/base.api';
import { EServer } from '../config/config';
import { EMsg } from '../services/message';
import { Request } from '../servers/Request';

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

let client: WebSocket[] = [];
wss.on('connection', (ws: WebSocket) => {
    client.push(ws);
    console.log(EMsg.clientConnect, client.length);

    ws.on('message', (message: string) => {
        const msg = JSON.parse(message.toString())
        console.log(EMsg.onMessage, msg);

        const request = new Request(msg)
        console.log(request.data);

        BaseApi.checkObject(request).then(result => {

            result.object = request.object;
            result.method = request.method;

            ws.send(JSON.stringify(result));

            console.log(EMsg.reply, JSON.stringify(result));

        }).catch(error => {
            console.log(error);
        })
    });

    ws.on('close', () => {
        console.log(EMsg.clientClose, client.length);

    })
});

function sendAll(message: string) {
    for (var i = 0; i < client.length; i++) {
        client[i].send("Message: " + message);
    }
}

server.listen(EServer.socketPort, EServer.allHost, () => {
    console.log(EMsg.socketRuning, EServer.socketPort);
});