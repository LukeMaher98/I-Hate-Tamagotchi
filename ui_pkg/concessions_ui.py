import PySimpleGUI as sg
from controllers import logic_controller
from entities import listings
from utils import utils

Heading = "TheAter Concessions"

concessions_info = utils.get_view_list("concessions","databases/concessions_db.txt")

concessions_list = listings.list_factory.create_list("concession",concessions_info)
concession_screen = concessions_list.generate_list()

concessionsBasket = logic_controller.logic.get_concessions_basket()

userLayout = [[sg.Text("TheAter Concessions")],
              [sg.Listbox(concession_screen, size=(50, 8), key='-LIST-', enable_events=True),
               sg.Listbox(concessionsBasket, size=(50, 8), key='-BASKET-', enable_events=True)],
              [sg.Button('Purchase Concessions')],
              [sg.Button('Back To Menu')]]
