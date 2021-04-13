import PySimpleGUI as sg
from utils import utils
from entities import listings
from entities import movie_factory

file = open('databases/screenings_db.txt', 'r')
screenings_info = file.readlines()

screenings_list = utils.get_movie_objetcs(screenings_info)

movie_list_output = []
for movie in screenings_list:
    output = ""
    output += "Screen " +movie.get_movie_screen()
    output += " - "+movie.get_movie_title()
    output += " : "+movie.get_movie_subtitled()
    output += " - "+movie.get_movie_type()
    output += " - Show Times -  "
    for showTime in movie.get_movie_showTimes() :
        output += showTime+" "
    movie_list_output.append(output)

layout = [[sg.Text('Double click or press Enter on selected screening to edit')],
            [sg.Listbox(movie_list_output, size=(100, len(movie_list_output)), key='-MOVIES-', bind_return_key=True)],
            [sg.Button('Save'), sg.Button('Add Screening'), sg.Button('Delete Selected'), sg.Button('Main Menu')]]

heading = "Edit Screenings"