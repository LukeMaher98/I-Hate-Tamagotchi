from utils import utils

# Facade Class for all of our different reader methods 
class Reader: 

    def read(self, filename, user):
        interaction = []
        if "ticket" in filename:
            interaction = utils.TicketSaleReader().read(filename)
        elif "concession_sales" in filename:
            interaction = utils.ConcessionSaleReader().read(filename)
        elif "concessions" in filename:
            interaction = utils.ConcessionReader().read(filename)
        elif user != "":
            interaction = utils.BookingsReader().read(filename, user)
        else:
            interaction = utils.BookingsReviewReader().read(filename)

        return interaction