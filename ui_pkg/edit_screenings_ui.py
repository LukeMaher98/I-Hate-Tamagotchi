import PySimpleGUI as sg
from utils import utils
from entities import listings

heading = "Edit Screenings"
movie_list_output = utils.get_movie_format()

layout = [[sg.Text('Double click or press Enter on selected screening to edit')],
            [sg.Listbox(movie_list_output, size=(100, 15), key='-MOVIES-', bind_return_key=True)],
            [sg.Button('Add Screening'), sg.Button('Delete Selected'), sg.Button('Main Menu')]]

