import PySimpleGUI as sg
from controllers import ui_controller, logic_controller
from utils import utils
import re
from entities import listings

concessionSales = utils.get_list("databases/concession_sales_db.txt")

def eventLoop(window, event, values):
    concFile = "databases/concessions_db.txt"
    saleFile = "databases/concession_sales_db.txt"

    if event == 'Main Menu':
        concessions_info = utils.get_view_list("concessions","databases/concessions_db.txt")
        concessions_list = listings.list_factory.create_list("concession",concessions_info)
        concession_screen = concessions_list.generate_list()
        window['-CONCESSIONS-'].update(values=concession_screen)
        backToMenu()
    if event == 'Save':
        utils.save_to_file(concFile, window['-CONCESSIONS-'].get_list_values())
        utils.save_list(saleFile, concessionSales)
        sg.popup("Saved Concessions")
    if event == 'Add Concession':
        text = sg.popup_get_text("Add concession in format 'ConcessionName,Price'")
        if text != None:
            v = window['-CONCESSIONS-'].get_list_values() 
            m = convertToDisplayForm(text)
            v.append(m)
            s = appendToSales(text)
            if s != None:
                concessionSales.append(s)
            window['-CONCESSIONS-'].update(values=v)
        else:
            sg.popup("Concessions must be in format 'ConcessionName,Price'")
    if event == 'Delete Selected':
        try:
            d = values['-CONCESSIONS-'][0]
            v = deleteSelected(d, window['-CONCESSIONS-'].get_list_values())
            window['-CONCESSIONS-'].update(values=v)
        except:
            sg.popup("Select concession to be deleted first!") 
    if event == '-CONCESSIONS-':
        text = sg.popup_get_text("Edit concession in format 'ConcessionName,Price'",
            default_text=convertToEditForm(values['-CONCESSIONS-'][0]))
        if text != None:
            i = window['-CONCESSIONS-'].get_indexes()
            j = getMatchingIndex(values['-CONCESSIONS-'][0], concessionSales)
            v = window['-CONCESSIONS-'].get_list_values()
            try:
                m = convertToDisplayForm(text)
                v[i[0]] = m
                concessionSales[j] = editSales(text, concessionSales[j])
                window['-CONCESSIONS-'].update(values=v)
            except:
                return
        else:
            sg.popup("Concessions must be in format 'ConcessionName,Price'")

def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_admin_ui()
    logic_controller.logic.set_main_menu_admin_loop()

def convertToEditForm(input):
    element = input.split(":")
    output = element[0] + ","
    element[1] = element[1].replace(" ", "")
    output = output + element[1].removesuffix("e\n")

    return output

def convertToDisplayForm(input):
    element = input.split(",")
    output = element[0] + ":"
    if re.match("[0-9]+", element[1]):
        output += " "+ element[1] + "e\n"
        return output

def deleteSelected(delete, values):
    output = []
    for v in values:
        if v != delete:
            output.append(v)

    return output

def appendToSales(input):
    v = input.split(",")
    for c in concessionSales:
        n = c.split(",")
        if n[0] == v[0]:
            return None
    return(v[0]+",0,\n")

def editSales(new, old):
    n = new.split(",")
    o = old.split(",")

    output = n[0] + "," + o[1] + "," + o[2]
    return output

def getMatchingIndex(item, list):
    counter = 0
    i = item.split(":")
    for l in list:
        t = l.split(",")
        if t[0] == i[0]:
            return counter 
        counter = counter + 1
