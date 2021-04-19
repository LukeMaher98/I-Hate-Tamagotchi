from controllers import ui_controller, logic_controller
from utils import utils
import abc    

class Command(metaclass=abc.ABCMeta):
    # Interface for all concrete commands

    @abc.abstractmethod
    def execute(self):
        pass


class UserLoginCommand(Command) : 

    def __init__(self, receiver, username, usernames, password, passwords, window):
        self._receiver = receiver
        self._username = username
        self._usernames = usernames
        self._password = password
        self._passwords = passwords
        self._window = window
        

    def execute(self) :
        self._receiver.user_login(self._username, self._usernames, self._password, self._passwords, self._window)


class AdminLoginCommand(Command) : 

    def __init__(self, receiver, username, usernames, password, passwords, window):
        self._receiver = receiver
        self._username = username
        self._usernames = usernames
        self._password = password
        self._passwords = passwords
        self._window = window
        

    def execute(self) :
        self._receiver.admin_login(self._username, self._usernames, self._password, self._passwords, self._window)
    

#Reciever below
class Receiver :
    # Processes user input for password and logs in
    def user_login(self, username, usernames, password, passwords, window):
        if password == utils.decrypt(passwords[usernames.index(username)]):
            ui_controller.ui.get_current_ui().Hide()
            ui_controller.ui.open_main_menu_user_ui()
            ui_controller.ui.set_current_user(username)
            logic_controller.logic.set_current_user(username)
            logic_controller.logic.set_main_menu_user_loop()
            logic_controller.logic.set_auth_type("user")
        else:
            window['-OUTPUT-'].update("Entered password is invalid")

    # Processes user input for admin password and logs in
    def admin_login(self, username, usernames, password, passwords, window):
        if password == utils.decrypt(passwords[usernames.index(username)]):
            ui_controller.ui.get_current_ui().Hide()
            ui_controller.ui.open_main_menu_admin_ui()
            ui_controller.ui.set_current_user(username)
            logic_controller.logic.set_current_user(username)
            logic_controller.logic.set_main_menu_admin_loop()
            logic_controller.logic.set_auth_type("admin")
        else:
            window['-OUTPUT-'].update("Entered password is invalid")

class Invoker:
    # Sends request to command
    def __init__(self):
        self._commands = []

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()