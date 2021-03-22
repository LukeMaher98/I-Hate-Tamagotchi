from logic_pkg import entry_logic
from logic_pkg import main_menu_logic
from logic_pkg import edit_screenings_logic
from logic_pkg import edit_concessions_logic
from logic_pkg import screenings_logic
from logic_pkg import concessions_logic
from logic_pkg import ticket_sales_logic
from logic_pkg import concession_sales_logic
from logic_pkg import book_ticket_logic
from logic_pkg import purchase_ticket_logic
from logic_pkg import redeem_booking_logic
from logic_pkg import review_bookings_logic

class Logic_Controller:
    def __init__(self): 
        self._login_loop = entry_logic.loginEventLoop 
        self._signup_loop = entry_logic.signupEventLoop 
        self._main_menu_admin_loop = main_menu_logic.adminEventLoop 
        self._main_menu_user_loop = main_menu_logic.userEventLoop
        self._screenings_user_loop = screenings_logic.screeningsEventLoop
        self._concessions_user_loop = concessions_logic.concessionsEventLoop
        self._ticket_sales_admin_loop = ticket_sales_logic.ticketSalesEventLoop
        self._concession_sales_admin_loop = concession_sales_logic.concessionSalesEventLoop
        self._book_ticket_user_loop = book_ticket_logic.bookTicketLoop
        self._purchase_ticket_user_loop = purchase_ticket_logic.purchaseTicketLoop
        self._redeem_booking_user_loop = redeem_booking_logic.redeemBookingLoop
        self._review_booking_loop = review_bookings_logic.reviewBookingLoop
        self._current_user = None
        self._current_loop = self._login_loop
        self.concession_basket = []
        self.concession_subtotal = 0
        self._auth_type = None
        self._exit = False
        self._edit_screenings_loop = edit_screenings_logic.eventLoop
        self._edit_concessions_loop = edit_concessions_logic.eventLoop

    def set_login_loop(self):  
        self._current_loop = self._login_loop

    def set_signup_loop(self):  
        self._current_loop = self._signup_loop

    def set_current_user(self, username):
        self._current_user = username

    def set_main_menu_admin_loop(self):
        self._current_loop = self._main_menu_admin_loop

    def set_main_menu_user_loop(self):
        self._current_loop = self._main_menu_user_loop
    
    def set_screenings_user_loop(self):
        self._current_loop = self._screenings_user_loop
   
    def set_concessions_user_loop(self):
        self._current_loop = self._concessions_user_loop

    def set_ticket_sales_admin_loop(self):
        self._current_loop = self._ticket_sales_admin_loop

    def set_concession_sales_admin_loop(self):
        self._current_loop = self._concession_sales_admin_loop

    def set_book_ticket_user_loop(self):
        self._current_loop = self._book_ticket_user_loop

    def set_purchase_ticket_user_loop(self):
        self._current_loop = self._purchase_ticket_user_loop
    
    def set_redeem_booking_user_loop(self):
        self._current_loop = self._redeem_booking_user_loop

    def set_review_booking_loop(self):
        self._current_loop = self._review_booking_loop

    def set_edit_screenings_loop(self):
        self._current_loop = self._edit_screenings_loop

    def set_edit_concessions_loop(self):
        self._current_loop = self._edit_concessions_loop

    def get_current_loop(self):
        return self._current_loop

    def set_concessions_basket(self, basket):
        self.concession_basket = basket

    def get_concessions_basket(self):
        return self.concession_basket

    def set_concessions_subtotal(self, subtotal):
        self.concession_subtotal = subtotal

    def get_concessions_subtotal(self):
        return self.concession_subtotal

    def set_auth_type(self, auth_type):
        self._auth_type = auth_type

    def get_auth_type(self):
        return self._auth_type 

    def exit(self):
        self._exit = True 

    def get_exit(self):
        return self._exit 

logic = Logic_Controller()