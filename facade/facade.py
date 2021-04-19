from facade import readers

# Facade Class for all of our different reader methods 
class Reader: 

    def read(self, filename, user):
        data = []
        if "ticket" in filename:
            data = readers.TicketSaleReader().read(filename)
        elif "screenings" in filename:
            data = readers.ScrreningReader().read(filename)
        elif "concession_sales" in filename:
            data = readers.ConcessionSaleReader().read(filename)
        elif "concessions" in filename:
            data = readers.ConcessionReader().read(filename)
        elif user != "":
            data = readers.BookingsReader().read(filename, user)
        else:
            data = readers.BookingsReviewReader().read(filename)

        return data