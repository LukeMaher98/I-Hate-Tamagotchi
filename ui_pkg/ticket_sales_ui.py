import PySimpleGUI as sg
from utils import utils
from entities import listings
Heading = "TheAter Ticket Sales"

ticket_sales_info = utils.get_view_list("ticket sale","databases/ticket_sales_db.txt")

ticket_sales_list = listings.list_factory.create_list("ticket sale", ticket_sales_info)
ticket_sales_screen = ticket_sales_list.generate_list()


adminLayout = [[sg.Text("TheAter Ticket Sales")], 
             [sg.Listbox(ticket_sales_screen, size=(100, len(ticket_sales_screen)), key='-List-', enable_events=True)],
             [sg.Button('Back To Menu')]]