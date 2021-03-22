import PySimpleGUI as sg
from controllers import ui_controller, logic_controller
from utils import utils
from entities import listings

def eventLoop(window, event, values):
    file = "databases/screenings_db.txt"
    if event == 'Main Menu':
        screenings_info = utils.get_view_list("movies",file)
        movie_list = listings.list_factory.create_list("movie",screenings_info)
        movie_screen = movie_list.generate_list()
        window['-MOVIES-'].update(values=movie_screen)
        backToMenu()
    if event == 'Save':
        movies = window['-MOVIES-'].get_list_values()
        s = []
        for m in movies:
            s.append(utils.convertToSaveForm(m)+"\n")
        utils.save_list(file, s)
        sg.popup("Saved Screenings")
    if event == 'Add Screening':
        text = sg.popup_get_text("Add screening in format 'MovieTitle,Screen,Time1,...,TimeN")
        if text != None:
            v = window['-MOVIES-'].get_list_values()
            m = utils.convertToDisplayForm(text)
            if m.endswith(":  ") != True:
                v.append(m)
                window['-MOVIES-'].update(values=v)
            else:
                sg.popup("Screenings must be in format 'MovieTitle,Screen,Time1,...,TimeN")
    if event == 'Delete Selected':
        try:
            d = values['-MOVIES-'][0]
            v = utils.deleteSelected(d, window['-MOVIES-'].get_list_values())
            window['-MOVIES-'].update(values=v)
        except:
            sg.popup("Select Screening to be deleted first!") 
    if event == '-MOVIES-':
        text = sg.popup_get_text("Edit screening in format 'MovieTitle,Screen,Time1,...,TimeN",
            default_text=utils.convertToEditForm(values['-MOVIES-'][0]))
        if text != None:
            i = window['-MOVIES-'].get_indexes()
            v = window['-MOVIES-'].get_list_values()
            m = utils.convertToDisplayForm(text)
            if m.endswith(":") != True:
                v[i[0]] = m
                window['-MOVIES-'].update(values=v)
            else:
                sg.popup("Screenings must be in format 'MovieTitle,Screen,Time1,...,TimeN")

def backToMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_main_menu_admin_ui()
    logic_controller.logic.set_main_menu_admin_loop()
