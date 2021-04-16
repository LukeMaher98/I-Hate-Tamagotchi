import PySimpleGUI as sg
from entities import listings, facade

Heading = "TheAter Ticket Sales"
reader = facade.Reader()
ticket_sales_info = reader.read("databases/ticket_sales_db.txt", "")

ticket_sales_list = listings.list_factory.create_list("ticket sale", ticket_sales_info)
ticket_sales_screen = ticket_sales_list.generate_list()


adminLayout = [[sg.Text("TheAter Ticket Sales")], 
             [sg.Listbox(ticket_sales_screen, size=(100, len(ticket_sales_screen)), key='-List-', enable_events=True)],
             [sg.Button('Back To Menu')]]