import abc


class Listing(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def generate_list(self):
        pass

class MovieList(Listing):
    def __init__(self, filename):
        self.filename = filename

    def generate_list(self):
        full_list = []
        for file in self.filename:
            output = ""
            movie_info = file.get_movie_info()
            output +="Screen " +movie_info[1]+ " - "
            output += " "+ movie_info[0] + ":"
            i = 0
            while i < len(movie_info[2]):
                output += " "+ movie_info[2][i]
                i += 1
            full_list.append(output)
        return full_list

class ConcessionList(Listing):
    def __init__(self, filename):
        self.filename = filename

    def generate_list(self):
        full_list = []
        for file in self.filename:
            output = ""
            concession_info = file.get_concession_info()
            output +=concession_info[0]
            output += ":"+ concession_info[1]
            full_list.append(output)
        return full_list

class ConcessionSalesList(Listing):
    def __init__(self, filename):
        self.filename = filename

    def generate_list(self):
        full_list = []
        for file in self.filename:
            output = ""
            concession_sales_info = file.get_concession_sales_info()
            output += concession_sales_info[0]
            output += " "+ concession_sales_info[1]
            full_list.append(output)
        return full_list

class TicketSalesList(Listing):
    def __init__(self, filename):
        self.filename = filename

    def generate_list(self):
        full_list = []
        for file in self.filename:
            output = ""
            ticket_sales_info = file.get_ticket_sales_info()
            output +=ticket_sales_info[0]
            output += " "+ ticket_sales_info[1]
            full_list.append(output)
        return full_list

class ListFactory:
    def create_list(self,type,list_info):
        if type == "movie":
            return MovieList(list_info)
        if type == "concession":
            return ConcessionList(list_info)
        if type == "concession sale":
            return ConcessionSalesList(list_info)
        if type == "ticket sale":
            return TicketSalesList(list_info)

list_factory = ListFactory()