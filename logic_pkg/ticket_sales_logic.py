import PySimpleGUI as sg
from controllers import ui_controller, logic_controller
from bridge import listing_factory
from facade import facade

reader = facade.Reader()

def ticketSalesEventLoop(window, event, values):
    if event == 'Back To Menu':
        backToMenu()
    if event == '-List-':
        sg.popup('{} tickets'.format(values['-List-'][0]))
    if event == 'Update Values':
        ticket_sales_info = reader.read("databases/ticket_sales_db.txt", "")
        ticket_sales_list = listing_factory.factory.create_list("ticket sale", ticket_sales_info)
        ticket_sales_screen = ticket_sales_list.generate_list()
        window['-List-'].update(values=ticket_sales_screen)


def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_admin_ui()
    logic_controller.logic.set_main_menu_admin_loop()

