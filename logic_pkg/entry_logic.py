from controllers import ui_controller, logic_controller
from interceptors import encryption_interceptor
from command import command


def loginEventLoop(window, event, values):
    window['-OUTPUT-'].update("Please enter your login details")
    window['-USERNAME-'].update("")
    window['-PASSWORD-'].update("")
    if event == 'Exit':
        logic_controller.logic.exit()
    if event == 'Signup':
        goToSignup()
    if event == 'Confirm':
        if (values['-PASSWORD-'] != '') and (values['-USERNAME-'] != ''):
            validateLogin(window, values['-USERNAME-'], values['-PASSWORD-'])
        else:
            window['-OUTPUT-'].update("Invalid details entered")
    window['-USERNAME-'].update("")
    window['-PASSWORD-'].update("")

def signupEventLoop(window, event, values):
    window['-USERNAME-'].update("")
    window['-PASSWORD-'].update("")
    window['-CONFIRM-'].update("")
    if event == 'Exit':
        logic_controller.logic.exit()
    if event == 'Login':
        goToLogin()
    if event == 'Submit':
        if ((values['-PASSWORD-'] != '') and (values['-USERNAME-'] != '') and (values['-CONFIRM-'] != '')) and (values['-PASSWORD-'] == values['-CONFIRM-']):
            save_new_user_data(values['-USERNAME-'], values["-PASSWORD-"])
            goToLogin()
            window['-OUTPUT-'].update("User successfully created")
        else:
            window['-OUTPUT-'].update("Invalid details entered")
    window['-USERNAME-'].update("")
    window['-PASSWORD-'].update("")
    window['-CONFIRM-'].update("")

def goToLogin():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_login_ui()
    logic_controller.logic.set_login_loop()

def goToSignup():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_signup_ui()
    logic_controller.logic.set_signup_loop()

def validateLogin(window, username, password):
    loginData = open("databases/login_db.txt", "r")
    usernames = loginData.readline().split(",")
    passwords = loginData.readline().split(",")
    authTypes = loginData.readline().split(",")
    invoker = command.Invoker()
    receiver = command.Receiver()
    if username in usernames:
        if authTypes[usernames.index(username)] == "admin":
            admin_login = command.AdminLoginCommand(receiver, username, usernames, password, passwords, window)
            invoker.store_command(admin_login)
            invoker.execute_commands()
        else:
            user_login = command.UserLoginCommand(receiver, username, usernames, password, passwords, window)
            invoker.store_command(user_login)
            invoker.execute_commands()
    else:
        window['-OUTPUT-'].update("Entered username is invalid")

@encryption_interceptor.encryption_interceptor
def save_new_user_data(username, password):
    readData = open("databases/login_db.txt", "r")
    usernames = readData.readline()
    usernames += username
    usernames += ","
    usernames = usernames.replace("\n", "")
    passwords = readData.readline()
    passwords += password
    passwords += ","
    passwords = passwords.replace("\n", "")
    authTypes = readData.readline()
    authTypes += "user,"
    writeData = open("databases/login_db.txt", "w")  
    writeData.write(usernames)
    writeData.write("\n")
    writeData.write(passwords)
    writeData.write("\n")
    writeData.write(authTypes)
