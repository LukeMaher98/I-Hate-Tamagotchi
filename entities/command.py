from controllers import ui_controller, logic_controller
import abc    

class Command(metaclass=abc.ABCMeta):
    #interface for all concrete commands

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

class Invoker:
    # sends request to command
    def __init__(self):
        self._commands = []

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()