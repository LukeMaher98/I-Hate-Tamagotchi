import PySimpleGUI as sg
from controllers import ui_controller, logic_controller
from utils import utils

def purchaseTicketLoop(window, event, values):
    if event == 'Back To Menu':
        backToMenu()
    if event == 'Back To Screenings':
        screenings()
    if event == 'Purchase Ticket':
        try:
            title, time = utils.title_times_split(values['-List-'][0], False)
            buyTicket(title)
            sg.popup('Ticket purchased for: {} at {}'.format(title, time[0]))
            backToMenu()
        except:
            sg.popup("Select a time first")

def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_user_ui()
    logic_controller.logic.set_main_menu_user_loop()

def screenings():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_screening_ui()
    logic_controller.logic.set_screenings_user_loop()

def buyTicket(title):
    ticketSales = ""
    found = False
    with open("databases/ticket_sales_db.txt", "r") as db:
        for line in db:
            string = line.split(",")
            if title == string[0]:
                ticketSales += title+","+str(int(string[1]) + 1)+",\n"
                found = True
            else:
                ticketSales += line

    if not found:
        ticketSales += title+",1,\n"


    db = open("databases/ticket_sales_db.txt", "w")
    db.write(ticketSales)