import abc
from bridge import bridge

movie_format = bridge.MovieFormat()
concession_format = bridge.ConcessionFormat()


class List(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def generate_list(self):
        pass


class MovieList(List):
    def __init__(self, filename):
        self.filename = filename

    def generate_list(self):
        full_list = []
        for file in self.filename:
            m_listing = bridge.ProductListing(
                movie_format, file)
            full_list.append(m_listing.get_listing())
        return full_list


class ConcessionList(List):
    def __init__(self, filename):
        self.filename = filename

    def generate_list(self):
        full_list = []
        for file in self.filename[0]:
            full_list.append(bridge.ProductListing(
                concession_format, file).get_listing())
        return full_list

    def generate_dict(self):
        full_dict = {}
        for file in self.filename[0]:
            concession = bridge.ProductListing(
                concession_format, file).get_listing(True)
            full_dict[concession.specification()] = concession
        return full_dict


class ConcessionSalesList(List):
    def __init__(self, filename):
        self.filename = filename

    def generate_list(self):
        full_list = []
        for file in self.filename:
            full_list.append(bridge.SalesListing(
                concession_format, file).get_listing())
        return full_list


class TicketSalesList(List):
    def __init__(self, filename):
        self.filename = filename

    def generate_list(self):
        full_list = []
        for file in self.filename:
            full_list.append(bridge.SalesListing(
                movie_format, file).get_listing())
        return full_list


class ListFactory:
    def create_list(self, type, list_info):
        if type == "movie":
            return MovieList(list_info)
        if type == "concession":
            return ConcessionList(list_info)
        if type == "concession sale":
            return ConcessionSalesList(list_info)
        if type == "ticket sale":
            return TicketSalesList(list_info)


factory = ListFactory()
