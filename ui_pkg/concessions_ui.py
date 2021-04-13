import PySimpleGUI as sg
from controllers import logic_controller
from utils import utils
from entities import listings

concessions_info = utils.read_file("databases/concessions_db.txt")

concessions_list = listings.list_factory.create_list(
    "concession", concessions_info)
concessions_display = concessions_list.generate_list()

Heading = "TheAter Concessions"

concessionsBasket = logic_controller.logic.get_concessions_basket()

userLayout = [[sg.Text("TheAter Concessions")],
              [sg.Listbox(concessions_display, size=(50, 8), key='-LIST-', enable_events=True),
               sg.Listbox(concessionsBasket["items"], size=(50, 8), key='-BASKET-', enable_events=True)],
              [sg.Button('Undo Action'), sg.Button('Redo Action')],
              [sg.Button('Purchase Concessions')],
              [sg.Button('Back To Menu')]]
