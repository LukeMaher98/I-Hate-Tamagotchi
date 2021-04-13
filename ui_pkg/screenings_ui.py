import PySimpleGUI as sg
from utils import utils
from entities import listings
from entities import movie_factory

Heading = "TheAter Screenings"

file = open('databases/screenings_db.txt', 'r')
screenings_info = file.readlines()

screenings_list = utils.get_movie_objetcs(screenings_info)

movie_list_output = []
for movie in screenings_list:
    output = ""
    output += "Screen: " +movie.get_movie_screen()
    output += " "+movie.get_movie_title()
    output += " - "+movie.get_movie_subtitled()
    output += " - "+movie.get_movie_type()
    movie_list_output.append(output)

userLayout = [[sg.Text("TheAter Screenings")], 
             [sg.Listbox(movie_list_output, size=(100, len(movie_list_output)), key='-List-', bind_return_key=True)],
             [sg.Button('Book Ticket')],
             [sg.Button('Purchase Ticket')],
             [sg.Button('Back To Menu')]]