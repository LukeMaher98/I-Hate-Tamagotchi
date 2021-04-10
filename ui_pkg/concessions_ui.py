import PySimpleGUI as sg
from controllers import logic_controller
from entities import concession_builder as cb
from utils import utils

concessions_db = utils.read_file("databases/concessions_db.txt")

popcornBuilder = cb.PopcornBuilder()
nachoBuilder = cb.NachoBuilder()
colaBuilder = cb.ColaBuilder()
hotdogBuilder = cb.HotDogBuilder()
director = cb.Director()

concessions_list = []

if "popcorn" in concessions_db[0]:
    director.setBuilder(popcornBuilder)
    popcorn = director.getConcession()
    concessions_list.append(popcorn.specification())

if "nachos" in concessions_db[0]:
    director.setBuilder(nachoBuilder)
    nacho = director.getConcession()
    concessions_list.append(nacho.specification())

if "cola" in concessions_db[0]:
    director.setBuilder(colaBuilder)
    cola = director.getConcession()
    concessions_list.append(cola.specification())

if "hotdog" in concessions_db[0]:
    director.setBuilder(hotdogBuilder)
    hotdog = director.getConcession()
    concessions_list.append(hotdog.specification())

Heading = "TheAter Concessions"

concessionsBasket = logic_controller.logic.get_concessions_basket()

userLayout = [[sg.Text("TheAter Concessions")],
              [sg.Listbox(concessions_list, size=(50, 8), key='-LIST-', enable_events=True),
               sg.Listbox(concessionsBasket, size=(50, 8), key='-BASKET-', enable_events=True)],
              [sg.Button('Purchase Concessions')],
              [sg.Button('Back To Menu')]]
