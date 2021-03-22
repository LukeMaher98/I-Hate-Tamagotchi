import PySimpleGUI as sg
from utils import utils
from entities import listings

concessions_info = utils.get_view_list("concessions","databases/concessions_db.txt")

concessions_list = listings.list_factory.create_list("concession",concessions_info)
concession_screen = concessions_list.generate_list()

layout = [[sg.Text('Double click or press Enter on selected concession to edit')],
            [sg.Listbox(concession_screen, size=(100, len(concession_screen)), key='-CONCESSIONS-', bind_return_key=True)],
            [sg.Button('Save'), sg.Button('Add Concession'), sg.Button('Delete Selected'), sg.Button('Main Menu')]]

heading = "Edit Concessions"