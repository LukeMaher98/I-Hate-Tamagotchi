import PySimpleGUI as sg
from ui_pkg import entry_ui
from ui_pkg import main_menu_ui
from ui_pkg import edit_screenings_ui
from ui_pkg import edit_concessions_ui
from ui_pkg import screenings_ui
from ui_pkg import concessions_ui
from ui_pkg import ticket_sales_ui
from ui_pkg import concession_sales_ui
from ui_pkg import book_ticket_ui
from ui_pkg import purchase_ticket_ui
from ui_pkg import redeem_booking_ui
from ui_pkg import review_bookings_ui

class UI_Controller:
    def __init__(self): 
        self._login_ui = sg.Window(entry_ui.loginHeading, entry_ui.loginLayout, finalize=True) 
        self._signup_ui = None 
        self._main_menu_admin_ui = None 
        self._main_menu_user_ui = None
        self._edit_screenings_ui = None
        self._edit_concessions_ui = None
        self._screenings_ui = None
        self._concessions_ui = None
        self._ticket_sales_ui = None
        self._concession_sales_ui = None
        self._book_ticket_ui = None
        self._purchase_ticket_ui = None
        self._redeem_booking_ui = None
        self._review_booking_ui = None
        self._current_user = None
        self._current_ui = self._login_ui  

    def open_login_ui(self):
        self._current_ui = self._login_ui

    def open_signup_ui(self):
        if self._signup_ui == None:
            self._signup_ui = sg.Window(entry_ui.signupHeading, entry_ui.signupLayout, finalize=True)
        self._current_ui = self._signup_ui

    def set_current_user(self, username):
        self._current_user = username

    def open_main_menu_admin_ui(self):
        if self._main_menu_admin_ui == None:
            self._main_menu_admin_ui = sg.Window(main_menu_ui.adminHeading, main_menu_ui.adminLayout, finalize=True)
        self._current_ui = self._main_menu_admin_ui

    def open_main_menu_user_ui(self):
        if self._main_menu_user_ui == None:
            self._main_menu_user_ui = sg.Window(main_menu_ui.userHeading, main_menu_ui.userLayout, finalize=True)
        self._current_ui = self._main_menu_user_ui
    
    def open_screening_ui(self):
        if self._screenings_ui == None:
            self._screenings_ui = sg.Window(screenings_ui.Heading, screenings_ui.userLayout, finalize=True)
        self._current_ui = self._screenings_ui

    def open_concessions_ui(self):
        if self._concessions_ui == None:
            self._concessions_ui = sg.Window(concessions_ui.Heading, concessions_ui.userLayout, finalize=True)
        self._current_ui = self._concessions_ui
    
    def open_ticket_sales_ui(self):
        if self._ticket_sales_ui == None:
            self._ticket_sales_ui = sg.Window(ticket_sales_ui.Heading, ticket_sales_ui.adminLayout, finalize=True)
        self._current_ui = self._ticket_sales_ui

    def open_concession_sales_ui(self):
        if self._concession_sales_ui == None:
            self._concession_sales_ui = sg.Window(concession_sales_ui.Heading, concession_sales_ui.adminLayout, finalize=True)
        self._current_ui = self._concession_sales_ui

    def open_book_ticket_ui(self, movie):
        self._book_ticket_ui = sg.Window(book_ticket_ui.Heading, book_ticket_ui.showLayout(movie), finalize=True)
        self._current_ui = self._book_ticket_ui

    def open_purchase_ticket_ui(self, movie):
        self._purchase_ticket_ui = sg.Window(purchase_ticket_ui.Heading, purchase_ticket_ui.showLayout(movie), finalize=True)
        self._current_ui = self._purchase_ticket_ui
    
    def open_redeem_booking_ui(self):
        self._redeem_booking_ui = sg.Window(redeem_booking_ui.Heading, redeem_booking_ui.showLayout(), finalize=True)
        self._current_ui = self._redeem_booking_ui

    def open_review_bookings_loop(self):
        self._review_booking_ui = sg.Window(review_bookings_ui.Heading, review_bookings_ui.showLayout(), finalize=True)
        self._current_ui = self._review_booking_ui

    def open_edit_screenings_ui(self):
        if self._edit_screenings_ui == None:
            self._edit_screenings_ui = sg.Window(edit_screenings_ui.heading, edit_screenings_ui.layout, finalize=True)
        self._current_ui = self._edit_screenings_ui
    
    def open_edit_concessions_ui(self):
        if self._edit_concessions_ui == None:
            self._edit_concessions_ui = sg.Window(edit_concessions_ui.heading, edit_concessions_ui.layout, finalize=True)
        self._current_ui = self._edit_concessions_ui

    def get_current_ui(self):
        return self._current_ui

ui = UI_Controller()