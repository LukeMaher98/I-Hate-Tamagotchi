import PySimpleGUI as sg
from bridge import listing_factory
from facade import facade

Heading = "TheAter Ticket Sales"
reader = facade.Reader()
ticket_sales_list = reader.read("databases/ticket_sales_db.txt", "")
ticket_sales_screen = ticket_sales_list.generate_list()

adminLayout = [[sg.Text("TheAter Ticket Sales")], 
             [sg.Listbox(ticket_sales_screen, size=(100, len(ticket_sales_screen)), key='-List-', enable_events=True)],
             [sg.Button('Update Values'), sg.Button('Back To Menu')]]