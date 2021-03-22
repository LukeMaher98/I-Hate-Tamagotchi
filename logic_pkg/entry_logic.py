from controllers import ui_controller, logic_controller
import requests


def loginEventLoop(window, event, values):
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
            requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
                "login": "failed",
                "Reason": "Other"
            })
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
            requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
                "signup": True,
            })
        else:
            window['-OUTPUT-'].update("Invalid details entered")
    window['-USERNAME-'].update("")
    window['-PASSWORD-'].update("")
    window['-CONFIRM-'].update("")

def adminLogin(username):
    requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
        "login": "true",
        "AccountType":"Admin"
    })
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_admin_ui()
    ui_controller.ui.set_current_user(username)
    logic_controller.logic.set_current_user(username)
    logic_controller.logic.set_main_menu_admin_loop()
    logic_controller.logic.set_auth_type("admin")

def userLogin(username):
    requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
        "login": "true",
        "AccountType":"Customer"
    })
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_user_ui()
    ui_controller.ui.set_current_user(username)
    logic_controller.logic.set_current_user(username)
    logic_controller.logic.set_main_menu_user_loop()
    logic_controller.logic.set_auth_type("user")

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
    if username in usernames:
        if password == passwords[usernames.index(username)]:
            if authTypes[usernames.index(username)] == "admin":
                adminLogin(username)
            else:
                userLogin(username)
        else:
            window['-OUTPUT-'].update("Entered password is invalid")
            requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
                "login": "failed",
                "Reason": "Password Invalid"
            })
    else:
        window['-OUTPUT-'].update("Entered username is invalid")
        requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
            "login": "failed",
            "Reason": "Username Invalid"
        })

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
