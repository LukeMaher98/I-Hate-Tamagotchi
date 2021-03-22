import PySimpleGUI as sg
from controllers import logic_controller
from utils import utils

Heading = "TheAter My Bookings"

def showLayout():
    bookingsInfo = utils.read_bookings(logic_controller.logic._current_user)
    
    return [[sg.Text("My Bookings")], 
             [sg.Listbox(bookingsInfo, size=(100, len(bookingsInfo)), key='-List-', enable_events=True)],
             [sg.Button('Redeem Booking')],
             [sg.Button('Back To Menu')]]