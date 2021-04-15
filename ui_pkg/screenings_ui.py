import PySimpleGUI as sg
from utils import utils
from entities import listings

Heading = "TheAter Screenings"
movie_list_output = utils.get_movie_format()


userLayout = [[sg.Text("TheAter Screenings")], 
             [sg.Listbox(movie_list_output, size=(100, 15), key='-List-', bind_return_key=True)],
             [sg.Button('Update')],
             [sg.Button('Book Ticket')],
             [sg.Button('Purchase Ticket')],
             [sg.Button('Back To Menu')]]