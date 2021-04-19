import PySimpleGUI as sg
from controllers import ui_controller, logic_controller
from bridge import listing_factory
from facade import facade
from utils import utils
from interceptors import concession_interceptor


reader = facade.Reader()
concessions_info = reader.read("databases/concessions_db.txt", "")

concessions_list = listing_factory.factory.create_list(
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
            #remove find item in dictionary by name
            item = values['-BASKET-'][0].split(",")
            myList = list(concessions_dict)

            for i in myList:
                i = i.split(",")
                if i[0] == item[0]:
                    item = i[0] + "," + i[1] + "," + i[2]
                    break

            concession_object = concessions_dict[item]
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

@concession_interceptor.concession_interceptor
def removeFromConcessionsBasket(window, concession_object):
    basket = logic_controller.logic.get_concessions_basket()
    basket["items"].remove(concession_object.specification())
    basket["subtotal"] -= concession_object.getPrice()
    logic_controller.logic.set_concessions_basket(basket)
    window['-BASKET-'].update(
        logic_controller.logic.get_concessions_basket()["items"])

@concession_interceptor.concession_interceptor
def undo_basket(window):
    logic_controller.logic.undo_concessions_basket()
    window['-BASKET-'].update(
        logic_controller.logic.get_concessions_basket()["items"])

@concession_interceptor.concession_interceptor
def redo_basket(window):
    logic_controller.logic.redo_concessions_basket()
    window['-BASKET-'].update(
        logic_controller.logic.get_concessions_basket()["items"])


# Concession Sales are incremented or added to the database of sales
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

    with open("databases/concession_sales_db.txt", "w") as db:
        db.write(concessionSales)

def emptyBasket(window):
    logic_controller.logic.empty_concessions_basket()
    window['-BASKET-'].update(
        logic_controller.logic.get_concessions_basket()["items"])
