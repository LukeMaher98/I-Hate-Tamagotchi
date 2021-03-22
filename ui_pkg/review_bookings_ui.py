import PySimpleGUI as sg
from utils import utils

Heading = "TheAter Bookings Review"

def showLayout():
    bookingsInfo = utils.read_bookings_review()
    
    return [[sg.Text("Bookings Review")], 
             [sg.Listbox(bookingsInfo, size=(100, len(bookingsInfo)), key='-List-', enable_events=True)],
             [sg.Button('Back To Menu')]]