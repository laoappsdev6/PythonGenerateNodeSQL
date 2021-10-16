import json
from config.config import MyConfig
from database.databaseCreation import DatabaseCreation
from database.tableCreation import TableCreation
from manage.handle import MyHandle


class Main:

    def start(self, dataJson):

        projectPath = dataJson["path"]
        projectName = dataJson["project"]
        projectDetail = dataJson["detail"]

        #create database
        if DatabaseCreation.create(projectName):

            #create table
            if TableCreation.create(projectName, projectDetail):

                #create file
                MyHandle.handle(projectPath, projectName, projectDetail)

            else:
                print("NO")
        else:
            print("NO")

if __name__ == '__main__':
    with open(MyConfig.jsonPath) as jsonFile:
        dataJson = json.load(jsonFile)
        main = Main()
        main.start(dataJson)
        jsonFile.close()