import PySimpleGUI as sg
from facade import facade

Heading = "TheAter Bookings Review"
reader = facade.Reader()

def showLayout():
    bookingsInfo = reader.read("databases/bookings_db.txt","")
    
    return [[sg.Text("Bookings Review")], 
             [sg.Listbox(bookingsInfo, size=(100, len(bookingsInfo)), key='-List-', enable_events=True)],
             [sg.Button('Back To Menu')]]