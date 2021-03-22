import PySimpleGUI as sg
from controllers import logic_controller, ui_controller
from utils import utils
import requests

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
    requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
            "Booking": "Success",
        })