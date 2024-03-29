import PySimpleGUI as sg
from controllers import ui_controller, logic_controller
from utils import utils

def eventLoop(window, event, values):
    file = "databases/screenings_db.txt"
    if event == 'Main Menu':
        backToMenu()
    if event == '-MOVIES-':
        sg.popup('{}'.format(values['-MOVIES-'][0]))
    if event == 'Add Screening':
        text = sg.popup_get_text("Add screening in format 'MovieTitle,Screen No,2D or 3D,Subtitled or Not Subtitled,Time1,...,TimeN,'")
        warning_text = "Screenings must be in format ''MovieTitle,Screen No,2D or 3D,Subtitled or Not Subtitled,Time1,...,TimeN,'"
        if text != None :
            if text != "" :
                format = utils.verify_format(text)
                if format != False:
                    utils.append_to_file("databases/screenings_db.txt",text)
                    movie_display = utils.getMovieListings()
                    window['-MOVIES-'].update(values=movie_display)
                else:
                    sg.popup(warning_text)
            else:
                sg.popup(warning_text)
    if event == 'Delete Selected':
        try:
            d = values['-MOVIES-'][0]
            utils.deleteSelected(d, window['-MOVIES-'].get_list_values(), file)
            movie_display = utils.getMovieListings()
            window['-MOVIES-'].update(values=movie_display)
        except:
            sg.popup("Select Screening to be deleted first!") 

def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_admin_ui()
    logic_controller.logic.set_main_menu_admin_loop()
