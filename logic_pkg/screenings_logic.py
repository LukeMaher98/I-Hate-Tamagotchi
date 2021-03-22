import PySimpleGUI as sg
from controllers import ui_controller, logic_controller

def screeningsEventLoop(window, event, values):
    if event == 'Back To Menu':
        backToMenu()
    if event == 'Book Ticket':
        try:
            movie = values['-List-'][0]
            bookTicket(movie)
        except:
            sg.popup("Select a movie first")
    if event == 'Purchase Ticket':
        try:
            movie = values['-List-'][0]
            purchaseTicket(movie)
        except:
            sg.popup("Select a movie first")
    if event == '-List-':
        sg.popup('{}'.format(values['-List-'][0]))


def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_user_ui()
    logic_controller.logic.set_main_menu_user_loop()


def bookTicket(movie):
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_book_ticket_ui(movie)
    logic_controller.logic.set_book_ticket_user_loop()

def purchaseTicket(movie):
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_purchase_ticket_ui(movie)
    logic_controller.logic.set_purchase_ticket_user_loop()


