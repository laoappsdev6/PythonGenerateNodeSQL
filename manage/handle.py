import os
from config.config import MyConfig
from manage.fileCreate.apiCreation import ApiCreation
from manage.fileCreate.baseCreation import BaseCreation
from manage.fileCreate.configCreation import ConfigCreation
from manage.fileCreate.controllerCreation import ControllerCreation
from manage.fileCreate.documentCreation import DocumentCreation
from manage.fileCreate.methodCreation import MethodCreation
from manage.fileCreate.modelCreation import ModelCreation
from manage.fileCreate.objectCreation import ObjectCreation
from manage.manage import MyManage
from model.directory import MyDir
from model.message import Msg
from model.name import Name
from model.status import FileSync


class MyHandle:

    @staticmethod
    def handle(path: str, project: str, detail: dict):

        # create directory
        if MyManage.makeDirectory(path, project):

            # copy default file
            if MyManage.copyFileDefault(MyConfig.fileDefaultPath, project, path):

                fileKey = detail.keys()

                # create base api file
                fileConfigName, contentConfig = ConfigCreation.create(project)
                configSetting = FileSync.replace
                pathConfig = os.path.join(path, project, MyDir.src, MyDir.config, fileConfigName)
                if MyManage.makeFile(pathConfig, contentConfig, configSetting):

                    # create base api file
                    fileBaseName, contentBase = BaseCreation.create(fileKey)
                    baseSetting = FileSync.replace
                    pathBase = os.path.join(path, project, MyDir.src, MyDir.api, fileBaseName)
                    if MyManage.makeFile(pathBase, contentBase, baseSetting):

                        # create object file
                        fileObjectName, contentObject = ObjectCreation.create(fileKey)
                        objectSetting = FileSync.replace
                        pathObject = os.path.join(path, project, MyDir.src, MyDir.service, fileObjectName)
                        if MyManage.makeFile(pathObject, contentObject, objectSetting):

                            # create method file
                            fileMethodName, contentMethod = MethodCreation.create(detail)
                            methodSetting = FileSync.replace
                            pathMethod = os.path.join(path, project, MyDir.src, MyDir.service, fileMethodName)
                            if MyManage.makeFile(pathMethod, contentMethod, methodSetting):

                                for className in fileKey:
                                    myDataField = detail[className][Name.field]
                                    apiSetting = detail[className][Name.setting][Name.apiSync]
                                    controllerSetting = detail[className][Name.setting][Name.controllerSync]
                                    modelSetting = detail[className][Name.setting][Name.modelSync]
                                    myDataFunction = detail[className][Name.function]

                                    # create model file
                                    fileModelName, contentModel = ModelCreation.create(className, myDataField)
                                    pathModel = os.path.join(path, project, MyDir.src, MyDir.model, fileModelName)
                                    if not MyManage.makeFile(pathModel, contentModel, modelSetting):
                                        print(Msg.makeFileFail.format(fileModelName))
                                        break

                                    # create controller file
                                    fileControllerName, contentController = ControllerCreation.create(className, myDataFunction, myDataField, detail)
                                    pathController = os.path.join(path, project, MyDir.src, MyDir.controller, fileControllerName)
                                    if not MyManage.makeFile(pathController, contentController, controllerSetting):
                                        print(Msg.makeFileFail.format(fileControllerName))
                                        break

                                    # create api file
                                    fileApiName, contentApi = ApiCreation.create(className, myDataFunction)
                                    pathApi = os.path.join(path, project, MyDir.src, MyDir.api, fileApiName)
                                    if not MyManage.makeFile(pathApi, contentApi, apiSetting):
                                        print(Msg.makeFileFail.format(fileApiName))
                                        break

                                    # create controller file
                                    fileDocumentName, contentDocument = DocumentCreation.create(className, myDataFunction, myDataField)
                                    documentSetting = FileSync.replace
                                    pathController = os.path.join(path, project, MyDir.src, MyDir.doc, fileDocumentName)
                                    if not MyManage.makeFile(pathController, contentDocument, documentSetting):
                                        print(Msg.makeFileFail.format(fileControllerName))
                                        break

                                # install project and open
                                pathModule = os.path.join(path, project, MyDir.node_modules)
                                if not os.path.exists(pathModule):
                                    npmProject = os.path.join(path, project)
                                    os.system(f"start \"\" cmd /k \"cd {npmProject} & npm install . & code . & exit;\n \\ & color 07\"")
                                print(Msg.success.format(project))

                            else:
                                print(Msg.makeFileFail.format(fileMethodName))
                        else:
                            print(Msg.makeFileFail.format(fileObjectName))
                    else:
                        print(Msg.makeFileFail.format(fileBaseName))
                else:
                    print(Msg.makeFileFail.format(fileConfigName))
            else:
                print(Msg.copyFileDefaultFail)
        else:
            print(Msg.makeDirectoryFail)
