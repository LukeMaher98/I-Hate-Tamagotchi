from utils import utils
from builder import builder
from abstract_factory import abstract_factory

popcornBuilder = builder.PopcornBuilder()
nachoBuilder = builder.NachoBuilder()
colaBuilder = builder.ColaBuilder()
hotdogBuilder = builder.HotDogBuilder()
director = builder.Director()

factoryStandard = abstract_factory.MovieStandard()
factorySubtitled = abstract_factory.MovieSubtitled()


class Format:
    def format_sales(self, data):
        pass

    def format_product(self, data, return_type=False):
        pass


class MovieFormat(Format):
    def format_sales(self, data):
        return data[0] + " " + data[1]

    def format_product(self, data, return_type=False):
        movie_info = data.split(',')
        show_times = []
        output = ""
        i = 4
        while i < len(movie_info)-1:
            output += " " + movie_info[i]
            i += 1
        show_times.append(output)

        if(movie_info[2] == "2D"):
            if(movie_info[3] == "Subtitled"):
                product = factorySubtitled.create_2D_movie(
                    movie_info[0], movie_info[1], show_times)
            else:
                product = factoryStandard.create_2D_movie(
                    movie_info[0], movie_info[1], show_times)
        if(movie_info[2] == "3D"):
            if(movie_info[3] == "Subtitled"):
                product = factorySubtitled.create_3D_movie(
                    movie_info[0], movie_info[1], show_times)
            else:
                product = factoryStandard.create_3D_movie(
                    movie_info[0], movie_info[1], show_times)
        if return_type == False:
            return product.get_movie_listing()
        else:
            return product


class ConcessionFormat(Format):
    def format_sales(self, data):
        return data[0] + " " + data[1]

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

    def get_listing(self, return_type=False):
        return self.format.format_sales(self.details)


class ProductListing(Listing):
    def __init__(self, Format, details):
        super().__init__(Format)
        self.details = details

    def get_listing(self, return_type=False):
        return self.format.format_product(self.details, return_type)
