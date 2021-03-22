class Movie:
    def __init__(self, movie_info):
        self.movie_info = movie_info

    def get_movie_info(self):
        return self.movie_info

class Concession:
    def __init__(self, concession_info):
        self.concession_info = concession_info

    def get_concession_info(self):
        return self.concession_info

class ConcessionSales:
    def __init__(self, concession_sales_info):
        self.concession_sales_info = concession_sales_info

    def get_concession_sales_info(self):
        return self.concession_sales_info

class TicketSales:
    def __init__(self, ticket_sales_info):
        self.ticket_sales_info = ticket_sales_info

    def get_ticket_sales_info(self):
        return self.ticket_sales_info