import PySimpleGUI as sg
from controllers import ui_controller, logic_controller
from utils import utils
from facade import facade

reader = facade.Reader()
filename = "databases/concessions_db.txt"

def eventLoop(window, event, values):
    if event == 'Main Menu':
        data = reader.read(filename, "")
        concession_screen = data[0]
        window['-CONCESSIONS-'].update(values=concession_screen)
        backToMenu()
    if event == 'Add Concession':
        data = reader.read(filename, "")
        if len(data) > 1:
            items = ''.join([str(elem) + "," for elem in data[1]])
            text = sg.popup_get_text(f"Add one of the following concessions: {items}")
            if text in data[1]:
                add_concession(filename, text)
                data = reader.read(filename, "")
                concession_screen = data[0]
                window['-CONCESSIONS-'].update(values=concession_screen)
            else:
                sg.popup(f"Concessions must be one of the following: {items}")
        else: 
            sg.popup(f"All Concessions have already been added")
    if event == 'Delete Selected':
        try:
            text = values['-CONCESSIONS-'][0]
            remove_concession(filename, text)
            data = reader.read(filename, "")
            concession_screen = data[0]
            window['-CONCESSIONS-'].update(values=concession_screen)
        except:
            sg.popup("Select concession to be deleted first!") 

def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_admin_ui()
    logic_controller.logic.set_main_menu_admin_loop()

def add_concession(filename, text):
    data = reader.read(filename, "")
    f = open(filename, "w")
    present = ''.join([str(elem) + "," for elem in data[0]])
    present += text + ",\n"

    data[1].remove(text)
    absent = ''.join([str(elem) + "," for elem in data[1]])

    f.write(present+absent)

def remove_concession(filename, text):
    data = reader.read(filename, "")
    f = open(filename, "w")

    data[0].remove(text)
    present = ''.join([str(elem) + "," for elem in data[0]])
    present += "\n"

    if len(data) > 1:
        absent = ''.join([str(elem) + "," for elem in data[1]])
        absent += text + ","
    else:
        absent = text + ","

    f.write(present+absent)


