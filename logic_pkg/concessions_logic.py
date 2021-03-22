import PySimpleGUI as sg
from controllers import ui_controller, logic_controller
import requests

def concessionsEventLoop(window, event, values):
    if event == 'Back To Menu':
        backToMenu()
    if event == 'Purchase Concessions':
        sg.popup(f'{"Subtotal: "}{logic_controller.logic.get_concessions_subtotal()}{"e"}')
        concessions = logic_controller.logic.get_concessions_basket()
        for item in concessions:
            title = item.split(":")[0]
            buyConcession(title)
        emptyBasket(window)
        backToMenu()
    if event == '-LIST-':
        amount = sg.popup_get_text("Select Amount")
        try:
            amount = int(amount)
            if amount > 0:
                for i in range(amount):
                    addToConcessionsBasket(window, values['-LIST-'][0])
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

def addToConcessionsBasket(window, value):
    concessions = logic_controller.logic.get_concessions_basket()
    concessions.append(value)
    logic_controller.logic.set_concessions_basket(concessions)
    subtotal = logic_controller.logic.get_concessions_subtotal()
    subtotal += parseItemPrice(value)
    logic_controller.logic.set_concessions_subtotal(subtotal)   
    window['-BASKET-'].update(logic_controller.logic.get_concessions_basket())

def removeFromConcessionsBasket(window, value):
    concessions = logic_controller.logic.get_concessions_basket()
    concessions.remove(value)
    logic_controller.logic.set_concessions_basket(concessions)
    subtotal = logic_controller.logic.get_concessions_subtotal()
    subtotal -= parseItemPrice(value)
    logic_controller.logic.set_concessions_subtotal(subtotal) 
    window['-BASKET-'].update(logic_controller.logic.get_concessions_basket())

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

    requests.post("https://logs-01.loggly.com/inputs/990e729b-d1a0-4ad1-a774-78d9c11a93c7/tag/http/", json={
            "ConcessionPurchased": "Success",
        })

    db = open("databases/concession_sales_db.txt", "w")
    db.write(concessionSales)

def emptyBasket(window):
    concessions = []
    logic_controller.logic.set_concessions_basket(concessions)
    window['-BASKET-'].update(logic_controller.logic.get_concessions_basket())

