import * as Net from 'net';
import { BaseApi } from '../api/base.api';
import { EServer } from '../config/config';
import { EMsg } from '../services/message';
import { Request } from '../servers/Request'

const client: Net.Socket[] = [];
const server = Net.createServer((socket) => {

    client.push(socket)
    console.log(EMsg.clientConnect, socket.remoteAddress, socket.remotePort);

    socket.on('close', (e) => {
        console.log(EMsg.clientClose, client.length);
    });

    socket.on('data', (message) => {
        const msg = JSON.parse(message.toString())
        console.log(EMsg.onMessage, msg);

        const request = new Request(msg)
        console.log(request.data);

        BaseApi.checkObject(request).then(result => {

            result.object = request.object;
            result.method = request.method;

            socket.write(JSON.stringify(result));

            console.log(EMsg.reply, JSON.stringify(result));

        }).catch(error => {
            console.log(error);
        })
    });
});

server.listen(EServer.tcpPort, EServer.allHost);
console.log(EMsg.tcpRuning, EServer.tcpPort);