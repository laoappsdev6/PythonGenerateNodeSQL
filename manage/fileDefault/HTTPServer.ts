import bodyParser from 'body-parser';
import cookieParser from 'cookie-parser';
import cors from 'cors';
import express from 'express';
import { BaseApi } from '../api/base.api';
import { EServer } from '../config/config';
import { EMsg } from '../services/message';
import { Request } from './Request';
const app = express();

app.use(bodyParser.json({ limit: '500mb' }));
app.use(bodyParser.urlencoded({ limit: '500mb', extended: true, parameterLimit: 50000 }));

app.use(cors());
app.use(cookieParser());

app.post("/", (req, res) => {

    console.log(EMsg.onMessage, req.body);

    const request = new Request(req.body)

    BaseApi.checkObject(request).then(result => {

        result.object = request.object;
        result.method = request.method;

        res.send(JSON.stringify(result));

        console.log(EMsg.reply, JSON.stringify(result));

    }).catch(error => {
        console.log(error);
    })
})

app.listen(EServer.httpPort, EServer.allHost, () => {
    console.log(EMsg.httpRuning, EServer.httpPort);
})