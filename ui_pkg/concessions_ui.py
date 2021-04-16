import PySimpleGUI as sg
from controllers import logic_controller
from entities import listings, facade

reader = facade.Reader()
concessions_info = reader.read("databases/concessions_db.txt", "")

concessions_list = listings.list_factory.create_list(
    "concession", concessions_info)
concessions_screen = concessions_list.generate_list()

Heading = "TheAter Concessions"

concessions_basket = logic_controller.logic.get_concessions_basket()

userLayout = [[sg.Text("TheAter Concessions")],
              [sg.Listbox(concessions_screen, size=(50, 8), key='-LIST-', enable_events=True),
               sg.Listbox(concessions_basket["items"], size=(50, 8), key='-BASKET-', enable_events=True)],
              [sg.Button('Undo Action'), sg.Button('Redo Action')],
              [sg.Button('Purchase Concessions')],
              [sg.Button('Back To Menu')]]
