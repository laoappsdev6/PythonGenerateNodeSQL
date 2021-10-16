import os
import shutil
from model.defaultList import DFList
from model.directory import MyDir
from model.status import FileSync


class MyManage:

    @staticmethod
    def makeDirectory(myPath: str, myProject: str) -> bool:

        try:
            srcPath = os.path.join(myPath, myProject, MyDir.src)
            apiPath = os.path.join(myPath, myProject, MyDir.src + "\\", MyDir.api)
            modelPath = os.path.join(myPath, myProject, MyDir.src + "\\", MyDir.model)
            controllerPath = os.path.join(myPath, myProject, MyDir.src + "\\", MyDir.controller)
            servicePath = os.path.join(myPath, myProject, MyDir.src + "\\", MyDir.service)
            configPath = os.path.join(myPath, myProject, MyDir.src + "\\", MyDir.config)
            serverPath = os.path.join(myPath, myProject, MyDir.src + "\\", MyDir.server)
            docPath = os.path.join(myPath, myProject, MyDir.src + "\\", MyDir.doc)

            if not os.path.exists(srcPath):
                os.makedirs(srcPath)
            if not os.path.exists(apiPath):
                os.makedirs(apiPath)
            if not os.path.exists(modelPath):
                os.makedirs(modelPath)
            if not os.path.exists(controllerPath):
                os.makedirs(controllerPath)
            if not os.path.exists(servicePath):
                os.makedirs(servicePath)
            if not os.path.exists(configPath):
                os.makedirs(configPath)
            if not os.path.exists(serverPath):
                os.makedirs(serverPath)
            if not os.path.exists(docPath):
                os.makedirs(docPath)
            return True

        except:
            return False

    @staticmethod
    def copyFileDefault(oldPath: str, project: str, newPath: str) -> bool:
        try:
            # Old Path
            httpServerPathOld = os.path.join(oldPath, DFList.httpServer)
            webSocketServerPathOld = os.path.join(oldPath, DFList.webSocketServer)
            tcpServerPathOld = os.path.join(oldPath, DFList.tcpServer)
            requestPathOld = os.path.join(oldPath, DFList.request)
            responsePathOld = os.path.join(oldPath, DFList.response)

            loginApiPathOld = os.path.join(oldPath, DFList.loginApi)

            authorizePathOld = os.path.join(oldPath, DFList.authorize)
            databasePathOld = os.path.join(oldPath, DFList.database)
            validateCPathOld = os.path.join(oldPath, DFList.validateC)

            loginModelPathOld = os.path.join(oldPath, DFList.loginModel)
            validateMPathOld = os.path.join(oldPath, DFList.validateM)

            servicePathOld = os.path.join(oldPath, DFList.service)
            messagePathOld = os.path.join(oldPath, DFList.message)

            packagePathOld = os.path.join(oldPath, DFList.package)
            tsconfigPathOld = os.path.join(oldPath, DFList.tsconfig)

            # New Path
            httpServerPathNew = os.path.join(newPath, project, MyDir.src, MyDir.server, DFList.httpServer)
            webSocketServerPathNew = os.path.join(newPath, project, MyDir.src, MyDir.server, DFList.webSocketServer)
            tcpServerPathNew = os.path.join(newPath, project, MyDir.src, MyDir.server, DFList.tcpServer)
            requestPathNew = os.path.join(newPath, project, MyDir.src, MyDir.server, DFList.request)
            responsePathNew = os.path.join(newPath, project, MyDir.src, MyDir.server, DFList.response)

            loginApiPathNew = os.path.join(newPath, project, MyDir.src, MyDir.api, DFList.loginApi)

            authorizePathNew = os.path.join(newPath, project, MyDir.src, MyDir.controller, DFList.authorize)
            databasePathNew = os.path.join(newPath, project, MyDir.src, MyDir.controller, DFList.database)
            validateCPathNew = os.path.join(newPath, project, MyDir.src, MyDir.controller, DFList.validateC)

            loginModelPathNew = os.path.join(newPath, project, MyDir.src, MyDir.model, DFList.loginModel)
            validateMPathNew = os.path.join(newPath, project, MyDir.src, MyDir.model, DFList.validateM)

            servicePathNew = os.path.join(newPath, project, MyDir.src, MyDir.service, DFList.service)
            messagePathNew = os.path.join(newPath, project, MyDir.src, MyDir.service, DFList.message)

            packagePathNew = os.path.join(newPath, project, DFList.package)
            tsconfigPathNew = os.path.join(newPath, project, DFList.tsconfig)

            if not os.path.exists(httpServerPathNew):
                shutil.copyfile(httpServerPathOld, httpServerPathNew)
            if not os.path.exists(webSocketServerPathNew):
                shutil.copyfile(webSocketServerPathOld, webSocketServerPathNew)
            if not os.path.exists(tcpServerPathNew):
                shutil.copyfile(tcpServerPathOld, tcpServerPathNew)
            if not os.path.exists(requestPathNew):
                shutil.copyfile(requestPathOld, requestPathNew)
            if not os.path.exists(responsePathNew):
                shutil.copyfile(responsePathOld, responsePathNew)
            if not os.path.exists(loginApiPathNew):
                shutil.copyfile(loginApiPathOld, loginApiPathNew)
            if not os.path.exists(authorizePathNew):
                shutil.copyfile(authorizePathOld, authorizePathNew)
            if not os.path.exists(databasePathNew):
                shutil.copyfile(databasePathOld, databasePathNew)
            if not os.path.exists(validateCPathNew):
                shutil.copyfile(validateCPathOld, validateCPathNew)
            if not os.path.exists(loginModelPathNew):
                shutil.copyfile(loginModelPathOld, loginModelPathNew)
            if not os.path.exists(validateMPathNew):
                shutil.copyfile(validateMPathOld, validateMPathNew)
            if not os.path.exists(servicePathNew):
                shutil.copyfile(servicePathOld, servicePathNew)
            if not os.path.exists(messagePathNew):
                shutil.copyfile(messagePathOld, messagePathNew)
            if not os.path.exists(packagePathNew):
                shutil.copyfile(packagePathOld, packagePathNew)
            if not os.path.exists(tsconfigPathNew):
                shutil.copyfile(tsconfigPathOld, tsconfigPathNew)

            return True
        except:
            return False

    @staticmethod
    def makeFile(pathFile: str, content: str, setting: str) -> bool:
        try:
            if setting == FileSync.replace:
                with open(pathFile, 'w') as f:
                    f.write(content)
                    f.close()
            else:
                if not os.path.exists(pathFile):
                    with open(pathFile, 'w') as f:
                        f.write(content)
                        f.close()
            return True
        except:
            return False
