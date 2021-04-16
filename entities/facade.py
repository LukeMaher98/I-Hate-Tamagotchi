from utils import utils

# Facade Class for all of our different reader methods 
class Reader: 

    def read(self, filename, user):
        data = []
        if "ticket" in filename:
            data = utils.TicketSaleReader().read(filename)
        elif "concession_sales" in filename:
            data = utils.ConcessionSaleReader().read(filename)
        elif "concessions" in filename:
            data = utils.ConcessionReader().read(filename)
        elif user != "":
            data = utils.BookingsReader().read(filename, user)
        else:
            data = utils.BookingsReviewReader().read(filename)

        return data