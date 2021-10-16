from model.name import Name


class MethodCreation:

    @staticmethod
    def create(allMethod: dict) -> str:
        fileName = "method.ts"
        methodKey = allMethod.keys()

        defaultMethod = """
export enum ELoginMethod {
    login = "authorize"
}
        """
        myMethod = ""
        for method in methodKey:
            manageMethod = allMethod[method][Name.function][Name.manage]
            listMethod = allMethod[method][Name.function][Name.list]
            manageKey = manageMethod.keys()
            listKey = listMethod.keys()
            allKey = manageKey | listKey

            methodDetail = MethodCreation.createDetail(allKey)

            methodContent = """
export enum E""" + f"""{method.capitalize()}""" + """Method {
    """ + f"""{methodDetail}""" + """
}
            """
            myMethod = myMethod + methodContent

        return fileName, defaultMethod + myMethod

    @staticmethod
    def createDetail(allKey: dict) -> str:
        methodDetail = ""
        for method in allKey:
            methodFormat = f"{method} = \"{method}\""
            methodDetail = methodDetail + methodFormat + ",\n"

        return methodDetail
