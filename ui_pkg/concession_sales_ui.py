import PySimpleGUI as sg
from entities import listings, facade

Heading = "TheAter Concession Sales"
reader = facade.Reader()
concession_sales_info = reader.read("databases/concession_sales_db.txt", "")

concession_sales_list = listings.list_factory.create_list("concession sale", concession_sales_info)
concession_sales_screen = concession_sales_list.generate_list()

adminLayout = [[sg.Text("TheAter Concession Sales")], 
             [sg.Listbox(concession_sales_screen, size=(100, len(concession_sales_screen)), key='-List-', enable_events=True)],
             [sg.Button('Update Values'), sg.Button('Back To Menu')]]