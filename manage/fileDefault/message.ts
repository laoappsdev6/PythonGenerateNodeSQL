export enum EMsg {
    socketRuning = "✨ 🎃 💘  Socket server is runing...  💘 🎃 ✨ on port: ",
    httpRuning = "✨ 🎃 💘  HTTP server is runing...  💘 🎃 ✨ on port: ",
    tcpRuning = "✨ 🎃 💘  TCP server is runing..  💘 🎃 ✨ on port: ",
    clientConnect = "✅✅ Client connection ✅✅ Id: ",
    clientClose = "❌❌ Client close ❌❌ Id: ",
    onMessage = "📩 📨 📧  Message from client  📧 📨 📩 Id: \n",
    reply = "🚀 🚀 🛫  Reply to client  🛫 🚀 🚀 Id: \n",


    loginSuccess = "Welcom to my application.",
    loginFail = "Sorry, Cannot login to the system!",
    objectNotFound = "Object not found!",
    methodNotFound = "Method not found!",
    noAuthorize = "You have no authorize",
    noUseSystem = "Sorry, You do not have access to the system!",
    noToken = "You have no token",
    wrongAccount = "Wrong username or password!",
    userEmpty = "Username is empty!",
    passEmpty = "Password is empty!",
    emptyUserAndPass = "Username and password are empty!",
    loginOk = "Login Successfully!",
    dataEmpty = "Data is empty!",


    addSuccess = "Add Data Successfully.",
    addFail = "Add Data Fail!",
    updateSuccess = "Update data successfully.",
    updateFail = "Update data fail!",
    deleteSuccess = "Delete data successfully.",
    deleteFail = "Delete data fail!",
    changePasswordSuccess = "Change Password Successfully.",
    changePasswordFail = "Change Password Fail!",


    listAll = "Data list all",
    listPage = "Data list page",
    listOne = "Data list one",


    objEmpty = "Data is empty!",
    empty = " is empty!",
    already = " already exists!",
    exists = " is not exists!",
    date = " is not date format!",
    time = " is not time format!",
    dateTime = " is not date time format!",
    number = " is number only!",
    notEqual = " is not equal ",
    mustBeThan = " must be more than ",
    validationError = "Validation error!",

}
export enum EStatus {
    success = 1,
    fail = 0
}