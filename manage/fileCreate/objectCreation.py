class ObjectCreation:

    @staticmethod
    def create(objectList: dict) -> str:
        fileName = "object.ts"

        objectDetail = ObjectCreation.createDetail(objectList)

        myBase = """
export enum EObject {
    login = "login",
   """+f"""{objectDetail}"""+"""
}
            """
        return fileName, myBase

    @staticmethod
    def createDetail(objectList: dict) -> str:
        objectDetail = ""
        for obj in objectList:

            objectFormat = f"{obj} = \"{obj}\""
            objectDetail = objectDetail + objectFormat + ",\n"

        return  objectDetail
