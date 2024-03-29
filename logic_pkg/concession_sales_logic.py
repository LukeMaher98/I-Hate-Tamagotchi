from os import read
import PySimpleGUI as sg
from controllers import ui_controller, logic_controller
from facade import facade

reader = facade.Reader()

def concessionSalesEventLoop(window, event, values):
    if event == 'Back To Menu':
        backToMenu()
    if event == '-List-':
        sg.popup('{} sales'.format(values['-List-'][0]))
    if event == 'Update Values':
        concession_sales_info = reader.read("databases/concession_sales_db.txt", "")
        concession_sales_screen = concession_sales_info.generate_list()
        window['-List-'].update(values=concession_sales_screen)


def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_admin_ui()
    logic_controller.logic.set_main_menu_admin_loop()

