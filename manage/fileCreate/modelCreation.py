class ModelCreation:

    @staticmethod
    def create(className: str, dataField: dict) -> str:
        fileName = className + ".model.ts"
        myClass = className.capitalize() + "Model"

        myProperty, myValidate = ModelCreation.createDetail(dataField)

        myModel = """
import { isEmpty, isNumber } from './validate.model';
""" + f"""
export class {myClass} 
""" + """
{
""" + f"""
{myProperty}
page: number;
limit: number;
""" + """

    constructor(data: Object) {
        Object.assign(this, data);
    }

    public validateAll(isAdd = true, isUpdate = false, isDelete = false): string {

        if (isUpdate || isDelete) {
            if (typeof this.id !== 'number') {
                return isNumber("id")
            }
        }
        if (isAdd || isUpdate) {  
""" + f"""
{myValidate}
""" + """
        }
        return "true";
    }
}
            """

        return fileName, myModel,

    @staticmethod
    def createDetail(data: dict) -> str:
        propertyKey = data.keys()
        myProperty = ""
        myValidate = ""

        for prop in propertyKey:

            dataType = data[prop]
            typeSplit = dataType[0:3]
            if typeSplit == "int":
                dataProp = prop + ": number;"
            elif typeSplit == "tin":
                dataProp = prop + ": boolean;"
            elif typeSplit == "dat":
                dataProp = prop + ": Date;"
            else:
                dataProp = prop + ": string;"
            myProperty = myProperty + dataProp + "\n"

            if prop != "id":
                validate = """if (!this.""" + f"""{prop}""" + """) { \n\t return isEmpty(\"""" + f"""{prop}""" + """\") \n}"""
                myValidate = myValidate + validate + "\n"

        return myProperty, myValidate
