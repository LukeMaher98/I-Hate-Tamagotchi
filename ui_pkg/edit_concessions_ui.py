import PySimpleGUI as sg
from facade import facade

reader = facade.Reader()
concession_screen = reader.read("databases/concessions_db.txt", "")
concession_screen = concession_screen[0]

layout = [[sg.Text('Add or remove concessions by selecting and using the buttons below')],
            [sg.Listbox(concession_screen, size=(100, 6), key='-CONCESSIONS-', bind_return_key=True)],
            [sg.Button('Add Concession'), sg.Button('Delete Selected'), sg.Button('Main Menu')]]

heading = "Edit Concessions"