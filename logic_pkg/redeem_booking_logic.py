import PySimpleGUI as sg
from controllers import ui_controller, logic_controller
from utils import utils

def redeemBookingLoop(window, event, values):
    if event == 'Back To Menu':
        backToMenu()
    if event == 'Redeem Booking':
        try:
            title, time = utils.title_times_split(values['-List-'][0], False)
            user = ui_controller.ui._current_user
            sg.popup('Booked ticket redeemed for: {} at {}'.format(title, time[0]))
            removeBooking(user, title, time[0])
            movie = values['-List-'][0]
            purchaseTicket(movie)
        except:
            sg.popup("Select a booking first")

def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_user_ui()
    logic_controller.logic.set_main_menu_user_loop()

def purchaseTicket(movie):
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_purchase_ticket_ui(movie)
    logic_controller.logic.set_purchase_ticket_user_loop()

def removeBooking(user, title, time):
    bookings = ""
    with open("databases/bookings_db.txt", "r") as db:
        for line in db:
            string = line.split(",")
            if user == string[0] and title == string[1] and time == string[2]:
                pass
            else: 
                bookings += string[0]+","+string[1]+","+string[2]+",\n"

    db = open("databases/bookings_db.txt", "w")
    db.write(bookings)
