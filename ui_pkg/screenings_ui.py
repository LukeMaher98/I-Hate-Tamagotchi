import PySimpleGUI as sg
from utils import utils
from entities import listings

Heading = "TheAter Screenings"
screenings_info = utils.get_view_list("movies","databases/screenings_db.txt")

movie_list = listings.list_factory.create_list("movie",screenings_info)
movie_screen = movie_list.generate_list()


userLayout = [[sg.Text("TheAter Screenings")], 
             [sg.Listbox(movie_screen, size=(100, len(movie_screen)), key='-List-', bind_return_key=True)],
             [sg.Button('Book Ticket')],
             [sg.Button('Purchase Ticket')],
             [sg.Button('Back To Menu')]]