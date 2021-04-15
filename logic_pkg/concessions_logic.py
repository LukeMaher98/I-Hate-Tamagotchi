import PySimpleGUI as sg
from controllers import ui_controller, logic_controller
from entities import concession_builder as cb
from entities import listings
import requests
from utils import utils
from interceptors import concession_interceptor


concessions_info = utils.read_file("databases/concessions_db.txt")

concessions_list = listings.list_factory.create_list(
    "concession", concessions_info)
concessions_dict = concessions_list.generate_dict()


def concessionsEventLoop(window, event, values):
    if event == 'Back To Menu':
        backToMenu()
    if event == 'Purchase Concessions':
        concessions = logic_controller.logic.get_concessions_basket()
        sg.popup(f'{"Subtotal: "}{concessions["subtotal"]}{"e"}')
        for item in concessions["items"]:
            buyConcession(item)
        emptyBasket(window)
        backToMenu()
    if event == 'Undo Action':
        undo_basket(window)
    if event == 'Redo Action':
        redo_basket(window)
    if event == '-LIST-':
        amount = sg.popup_get_text("Select Amount")
        try:
            amount = int(amount)
            if amount > 0:
                concession_object = concessions_dict[values['-LIST-'][0]]
                addToConcessionsBasket(window, concession_object, amount)
            else:
                sg.popup("Select a value greater than 0")
        except:
            sg.popup("Select a numeric value")
    if event == '-BASKET-':
        try:
            concession_object = concessions_dict[values['-BASKET-'][0]]
            removeFromConcessionsBasket(window, concession_object)
        except:
            sg.popup("No Items to remove")


def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_user_ui()
    logic_controller.logic.set_main_menu_user_loop()


@concession_interceptor.concession_interceptor
def addToConcessionsBasket(window, concession_object, amount):
    basket = logic_controller.logic.get_concessions_basket()
    for i in range(amount):
        basket["items"].append(concession_object.specification())
        basket["subtotal"] += concession_object.getPrice()
    logic_controller.logic.set_concessions_basket(basket)
    window['-BASKET-'].update(
        logic_controller.logic.get_concessions_basket()["items"])


def removeFromConcessionsBasket(window, concession_object):
    basket = logic_controller.logic.get_concessions_basket()
    basket["items"].remove(concession_object.specification())
    basket["subtotal"] -= concession_object.getPrice()
    logic_controller.logic.set_concessions_basket(basket)
    window['-BASKET-'].update(
        logic_controller.logic.get_concessions_basket()["items"])


def undo_basket(window):
    logic_controller.logic.undo_concessions_basket()
    window['-BASKET-'].update(
        logic_controller.logic.get_concessions_basket()["items"])


def redo_basket(window):
    logic_controller.logic.redo_concessions_basket()
    window['-BASKET-'].update(
        logic_controller.logic.get_concessions_basket()["items"])


def buyConcession(concession):
    concessionSales = ""
    found = False

    #extract name from concession object which is passed as string
    temp = concession.split(", ")
    temp = temp[0].split("Name: ")
    concession = temp[1]

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

    # requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
    #         "ConcessionPurchased": "Success",
    #     })

    with open("databases/concession_sales_db.txt", "w") as db:
        db.write(concessionSales)

def emptyBasket(window):
    logic_controller.logic.empty_concessions_basket()
    window['-BASKET-'].update(
        logic_controller.logic.get_concessions_basket()["items"])
