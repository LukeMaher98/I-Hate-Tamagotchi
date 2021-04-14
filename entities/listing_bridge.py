from utils import utils
from entities import concession_builder as cb

popcornBuilder = cb.PopcornBuilder()
nachoBuilder = cb.NachoBuilder()
colaBuilder = cb.ColaBuilder()
hotdogBuilder = cb.HotDogBuilder()
director = cb.Director()


class Format:
    def format_sales(self, data):
        pass

    def format_product(self, data):
        pass


class MovieFormat(Format):
    def format_sales(self, data):
        output = ""
        ticket_sales_info = data.get_ticket_sales_info()
        output += ticket_sales_info[0]
        output += " " + ticket_sales_info[1]
        return output

    def format_product(self, data, return_type=False):
        output = ""
        movie_info = data.get_movie_info()
        output += "Screen " + movie_info[1] + " - "
        output += " " + movie_info[0] + ":"
        i = 0
        while i < len(movie_info[2]):
            output += " " + movie_info[2][i]
            i += 1
        return output


class ConcessionFormat(Format):
    def format_sales(self, data):
        output = ""
        concession_sales_info = data.get_concession_sales_info()
        output += concession_sales_info[0]
        output += " " + concession_sales_info[1]
        return output

    def format_product(self, data, return_type=False):
        if data == "popcorn":
            director.setBuilder(popcornBuilder)
        if data == "nachos":
            director.setBuilder(nachoBuilder)
        if data == "cola":
            director.setBuilder(colaBuilder)
        if data == "hotdog":
            director.setBuilder(hotdogBuilder)
        product = director.getConcession()
        if return_type == False:
            return product.specification()
        else:
            return product


class Listing:
    def __init__(self, Format):
        self.format = Format

    def get_listing(self, return_type=False):
        pass


class SalesListing(Listing):
    def __init__(self, Format, details):
        super().__init__(Format)
        self.details = details

    def get_listing(self):
        return self.format.format_sales(self.details)


class ProductListing(Listing):
    def __init__(self, Format, details):
        super().__init__(Format)
        self.details = details

    def get_listing(self, return_type=False):
        return self.format.format_product(self.details, return_type)

