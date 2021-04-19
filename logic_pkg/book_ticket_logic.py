import PySimpleGUI as sg
from controllers import logic_controller, ui_controller
from utils import utils

def bookTicketLoop(window, event, values):
    if event == 'Back To Menu':
        backToMenu()
    if event == 'Back To Screenings':
        screenings()
    if event == 'Book Ticket':
        try:
            title, time = utils.title_times_split(values['-List-'][0], False)
            user = ui_controller.ui._current_user
            sg.popup('Ticket booked for: {} at {}'.format(title, time[0]))
            addBooking(user, title, time[0])
            backToMenu()
        except:
            sg.popup("Select a booking first")

def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_user_ui()
    logic_controller.logic.set_main_menu_user_loop()

def screenings():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_screening_ui()
    logic_controller.logic.set_screenings_user_loop()

def addBooking(user, title, time):
    booking = user+","+title+","+time+",\n"
    db = open("databases/bookings_db.txt", "a")
    db.write(booking)
