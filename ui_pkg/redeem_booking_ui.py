import PySimpleGUI as sg
from controllers import logic_controller
from entities import facade

Heading = "TheAter My Bookings"
reader = facade.Reader()

def showLayout():
    bookingsInfo = reader.read("databases/bookings_db.txt", logic_controller.logic._current_user)
    
    return [[sg.Text("My Bookings")], 
             [sg.Listbox(bookingsInfo, size=(100, len(bookingsInfo)), key='-List-', enable_events=True)],
             [sg.Button('Redeem Booking')],
             [sg.Button('Back To Menu')]]