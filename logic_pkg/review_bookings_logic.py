import PySimpleGUI as sg
from controllers import ui_controller, logic_controller

def reviewBookingLoop(window, event, values):
    if event == 'Back To Menu':
        backToMenu()

def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_admin_ui()
    logic_controller.logic.set_main_menu_admin_loop()
