from controllers import ui_controller, logic_controller

def adminEventLoop(window, event, values):
    if event == 'Logout':
        logout()
    if event == 'Alter Screenings':
        editScreeningsMenu()
    if event == 'Alter Concessions':
        editConcessionsMenu()
    if event == 'Bookings Review':
        reviewBookings()
    if event == 'View Ticket Sales':
        ticketSales()
    if event == 'View Concession Sales':
        concessionSales()

def userEventLoop(window, event, values):
    if event == 'Logout':
        logout()
    if event == 'Screenings':
        screenings()
    if event == 'Concessions':
        concessions()
    if event == 'My Bookings':
        myBookings()

def logout():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_login_ui()
    logic_controller.logic.set_login_loop()
    logic_controller.logic.set_auth_type(None)

def editScreeningsMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_edit_screenings_ui()
    logic_controller.logic.set_edit_screenings_loop()

def editConcessionsMenu():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_edit_concessions_ui()
    logic_controller.logic.set_edit_concessions_loop()
    
def screenings():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_screening_ui()
    logic_controller.logic.set_screenings_user_loop()


def concessions():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_concessions_ui()
    logic_controller.logic.set_concessions_user_loop()

def myBookings():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_redeem_booking_ui()
    logic_controller.logic.set_redeem_booking_user_loop()
    logic_controller.logic.set_auth_type("user")

def ticketSales():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_ticket_sales_ui()
    logic_controller.logic.set_ticket_sales_admin_loop()
    

def concessionSales():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_concession_sales_ui()
    logic_controller.logic.set_concession_sales_admin_loop()

def reviewBookings():
    ui_controller.ui.get_current_ui().Hide()
    ui_controller.ui.open_review_bookings_loop()
    logic_controller.logic.set_review_booking_loop()
