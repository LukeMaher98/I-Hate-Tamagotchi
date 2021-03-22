import PySimpleGUI as sg
from entities import listings
from utils import utils

Heading = "TheAter Concession Sales"
concession_sales_info = utils.get_view_list("concession sale","databases/concession_sales_db.txt")

concession_sales_list = listings.list_factory.create_list("concession sale", concession_sales_info)
concession_sales_screen = concession_sales_list.generate_list()

adminLayout = [[sg.Text("TheAter Concession Sales")], 
             [sg.Listbox(concession_sales_screen, size=(100, len(concession_sales_screen)), key='-List-', enable_events=True)],
             [sg.Button('Back To Menu')]]