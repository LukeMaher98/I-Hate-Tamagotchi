import PySimpleGUI as sg
from utils import utils
from entities import listings

screenings_info = utils.get_view_list("movies","databases/screenings_db.txt")

movie_list = listings.list_factory.create_list("movie",screenings_info)
movie_screen = movie_list.generate_list()

layout = [[sg.Text('Double click or press Enter on selected screening to edit')],
            [sg.Listbox(movie_screen, size=(100, len(movie_screen)), key='-MOVIES-', bind_return_key=True)],
            [sg.Button('Save'), sg.Button('Add Screening'), sg.Button('Delete Selected'), sg.Button('Main Menu')]]

heading = "Edit Screenings"