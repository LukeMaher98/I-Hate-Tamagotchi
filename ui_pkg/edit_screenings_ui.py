import PySimpleGUI as sg
from utils import utils

heading = "Edit Screenings"
movie_display = utils.getMovieListings()

layout = [[sg.Text('Double click or press Enter on selected screening to edit')],
            [sg.Listbox(movie_display, size=(100, 15), key='-MOVIES-', bind_return_key=True)],
            [sg.Button('Add Screening'), sg.Button('Delete Selected'), sg.Button('Main Menu')]]

