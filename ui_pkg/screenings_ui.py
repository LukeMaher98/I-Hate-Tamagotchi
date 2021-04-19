import PySimpleGUI as sg
from utils import utils

Heading = "TheAter Screenings"
movie_display = utils.getMovieListings()


userLayout = [[sg.Text("TheAter Screenings")],
              [sg.Listbox(movie_display, size=(100, 15),
                          key='-List-', bind_return_key=True)],
              [sg.Button('Update')],
              [sg.Button('Book Ticket')],
              [sg.Button('Purchase Ticket')],
              [sg.Button('Back To Menu')]]
