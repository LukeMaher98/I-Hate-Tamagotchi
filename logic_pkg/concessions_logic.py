import PySimpleGUI as sg
from controllers import ui_controller, logic_controller
import requests


def concessionsEventLoop(window, event, values):
    if event == 'Back To Menu':
        backToMenu()
    if event == 'Purchase Concessions':
        concessions = logic_controller.logic.get_concessions_basket()
        sg.popup(f'{"Subtotal: "}{concessions["subtotal"]}{"e"}')
        for item in concessions["items"]:
            title = item.split(": ")[1]
            name = title.split(',')[0]
            buyConcession(name)
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
                addToConcessionsBasket(window, values['-LIST-'][0], amount)
            else:
                sg.popup("Select a value greater than 0")
        except:
            sg.popup("Select a numeric value")
    if event == '-BASKET-':
        removeFromConcessionsBasket(window, values['-BASKET-'][0])


def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_user_ui()
    logic_controller.logic.set_main_menu_user_loop()


def addToConcessionsBasket(window, value, amount):
    basket = logic_controller.logic.get_concessions_basket()
    for i in range(amount):
        basket["items"].append(value)
        basket["subtotal"] += parseItemPrice(value)
    logic_controller.logic.set_concessions_basket(basket)
    window['-BASKET-'].update(
        logic_controller.logic.get_concessions_basket()["items"])


def removeFromConcessionsBasket(window, value):
    basket = logic_controller.logic.get_concessions_basket()
    basket["items"].remove(value)
    basket["subtotal"] -= parseItemPrice(value)
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


def parseItemPrice(value):
    strPrice = value[value.rfind(":"): value.rfind("e")]
    strPrice = strPrice.replace(":", "")
    strPrice = strPrice = strPrice.replace(" ", "")
    return int(strPrice)

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

    logic_controller.logic.set_concessions_basket({'items': [], 'subtotal': 0})

    # requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
    #         "ConcessionPurchased": "Success",
    #     })

    db = open("databases/concession_sales_db.txt", "w")
    db.write(concessionSales)


def emptyBasket(window):
    logic_controller.logic.set_concessions_basket({'items': [], 'subtotal': 0})
    window['-BASKET-'].update(
        logic_controller.logic.get_concessions_basket()["items"])
