import PySimpleGUI as sg
from utils import utils
from entities import listings

data = utils.read_file("databases/concessions_db.txt")
concession_screen = data[0]

layout = [[sg.Text('Double click or press Enter on selected concession to edit')],
            [sg.Listbox(concession_screen, size=(100, 6), key='-CONCESSIONS-', bind_return_key=True)],
            [sg.Button('Add Concession'), sg.Button('Delete Selected'), sg.Button('Main Menu')]]

heading = "Edit Concessions"