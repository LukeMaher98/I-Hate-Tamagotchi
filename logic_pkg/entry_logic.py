from controllers import ui_controller, logic_controller
import requests
import abc

class Invoker:
    # sends request to command
    def __init__(self):
        self._commands = []

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()

class Command(metaclass=abc.ABCMeta):
    #interface for all concrete commands
    def __init__(self, login):
        self._login = login

    @abc.abstractmethod
    def execute(self):
        pass


    #Define a binding between a Receiver object and an action.
    #Implement Execute by invoking the corresponding operation(s) on
    #Receiver. 
class UserLoginCommand(Command) : 

    def __init__(self, receiver, userName):
        self._receiver = receiver
        self._userName = userName


    def execute(self) :
        self._receiver.user_login(self._userName)


class AdminLoginCommand(Command) : 

    def __init__(self, receiver, userName):
        self._receiver = receiver
        self._userName = userName


    def execute(self) :
        self._receiver.admin_login(self._userName)
    

#Reciever below
class Receiver :
    
    def user_login(self, userName):
        ui_controller.ui.get_current_ui().Hide()
        ui_controller.ui.open_main_menu_user_ui()
        ui_controller.ui.set_current_user(userName)
        logic_controller.logic.set_current_user(userName)
        logic_controller.logic.set_main_menu_user_loop()
        logic_controller.logic.set_auth_type("user")

    def admin_login(self, userName):
        ui_controller.ui.get_current_ui().Hide()
        ui_controller.ui.open_main_menu_admin_ui()
        ui_controller.ui.set_current_user(userName)
        logic_controller.logic.set_current_user(userName)
        logic_controller.logic.set_main_menu_admin_loop()
        logic_controller.logic.set_auth_type("admin")  

    

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
    receiver = Receiver()
    invoker = Invoker()
    if username in usernames:
        if password == passwords[usernames.index(username)]:
            if authTypes[usernames.index(username)] == "admin":
                admin_login = AdminLoginCommand(receiver, username)
                invoker.store_command(admin_login)
                invoker.execute_commands()
            else:
                user_login = UserLoginCommand(receiver, username)
                invoker.store_command(user_login)
                invoker.execute_commands()
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
