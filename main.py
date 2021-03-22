import PySimpleGUI as sg
from controllers import ui_controller, logic_controller

sg.theme('BluePurple')
while True:
    if logic_controller.logic.get_exit() == True:
        break

    window = ui_controller.ui.get_current_ui()
    eventLoop = logic_controller.logic.get_current_loop()
    window.UnHide()
    
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    eventLoop(window, event, values)

window.close()
