import PySimpleGUI as sg
from controllers import ui_controller, logic_controller
from entities import concession_builder as cb
import requests
from utils import utils


concessions_db = utils.read_file("databases/concessions_db.txt")
popcornBuilder = cb.PopcornBuilder()
nachoBuilder = cb.NachoBuilder()
colaBuilder = cb.ColaBuilder()
hotdogBuilder = cb.HotDogBuilder()
director = cb.Director()
concessions_dict = {}

director.setBuilder(popcornBuilder)
popcorn = director.getConcession()
concessions_dict[popcorn.specification()] = popcorn

director.setBuilder(nachoBuilder)
nacho = director.getConcession()
concessions_dict[nacho.specification()] = nacho

director.setBuilder(colaBuilder)
cola = director.getConcession()
concessions_dict[cola.specification()] = cola

director.setBuilder(hotdogBuilder)
hotdog = director.getConcession()
concessions_dict[hotdog.specification()] = hotdog



def concessionsEventLoop(window, event, values):
    if event == 'Back To Menu':
        backToMenu()
    if event == 'Purchase Concessions':
        sg.popup(f'{"Subtotal: "}{logic_controller.logic.get_concessions_subtotal()}{"e"}')
        concessions = logic_controller.logic.get_concessions_basket()
        for item in concessions:
            buyConcession(item)
        emptyBasket(window)
        backToMenu()
    if event == '-LIST-':
        amount = sg.popup_get_text("Select Amount")
        try:
            amount = int(amount)
            if amount > 0:
                for i in range(amount):
                    concession_object = concessions_dict[values['-LIST-'][0]]
                    addToConcessionsBasket(window, concession_object)
            else:
                sg.popup("Select a value greater than 0")
        except:
            sg.popup("Select a numeric value")
    if event == '-BASKET-':
        concession_object = concessions_dict[values['-LIST-'][0]]
        removeFromConcessionsBasket(window, concession_object)

def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_user_ui()
    logic_controller.logic.set_main_menu_user_loop()

def addToConcessionsBasket(window, concession_object):
    concessions = logic_controller.logic.get_concessions_basket()
    concessions.append(concession_object.getName())
    logic_controller.logic.set_concessions_basket(concessions)
    subtotal = logic_controller.logic.get_concessions_subtotal()
    subtotal += concession_object.getPrice()
    logic_controller.logic.set_concessions_subtotal(subtotal)   
    window['-BASKET-'].update(logic_controller.logic.get_concessions_basket())

def removeFromConcessionsBasket(window, concession_object):
    concessions = logic_controller.logic.get_concessions_basket()
    concessions.remove(concession_object.getName())
    logic_controller.logic.set_concessions_basket(concessions)
    subtotal = logic_controller.logic.get_concessions_subtotal()
    subtotal -= concession_object.getPrice()
    logic_controller.logic.set_concessions_subtotal(subtotal) 
    window['-BASKET-'].update(logic_controller.logic.get_concessions_basket())


def buyConcession(concession):
    concessionSales = ""
    found = False
    with open("databases/concession_sales_db.txt", "r") as db:
        for line in db:
            string = line.split(",")
            if concession == string[0]:
                concessionSales += concession+","+str(int(string[1]) + 1)+",\n"
                found = True
            else:
                concessionSales += line

    if not found:
        concessionSales += concession+",1,\n"

    subtotal = 0
    logic_controller.logic.set_concessions_subtotal(subtotal)

    # requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
    #         "ConcessionPurchased": "Success",
    #     })

    db = open("databases/concession_sales_db.txt", "w")
    db.write(concessionSales)

def emptyBasket(window):
    concessions = []
    logic_controller.logic.set_concessions_basket(concessions)
    window['-BASKET-'].update(logic_controller.logic.get_concessions_basket())

