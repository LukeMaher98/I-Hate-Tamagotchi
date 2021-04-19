from __future__ import annotations
import abc
from abc import ABC, abstractmethod

# Interface for operations
class AbstractFactory(ABC):
    @abstractmethod
    def create_2D_movie(self) -> AbstractMovie2D:
        pass

    @abstractmethod
    def create_3D_movie(self) -> AbstractMovie3D:
        pass

# Two concrete factories that implement AbstractFactory interface
class MovieStandard(AbstractFactory):

    def create_2D_movie(self, name, screen, showTimes) -> AbstractMovie2D:
        return Movie2D(name, screen, showTimes)

    def create_3D_movie(self, name, screen, showTimes) -> AbstractMovie3D:
        return Movie3D(name, screen, showTimes)


class MovieSubtitled(AbstractFactory):

    def create_2D_movie(self, name, screen, showTimes) -> AbstractMovie2D:
        return SubtitledMovie2D(name, screen, showTimes)

    def create_3D_movie(self, name, screen, showTimes) -> AbstractMovie3D:
        return SubtitledMovie3D(name, screen, showTimes)

# Interface for movie2D product
class AbstractMovie2D(ABC):

    @abstractmethod
    def get_movie_title(self) :
        pass
    @abstractmethod
    def get_movie_screen(self):
        pass
    @abstractmethod
    def get_movie_subtitled(self) :
        pass
    @abstractmethod
    def get_movie_type(self):
        pass
    @abstractmethod
    def get_movie_showTimes(self):
        pass

# products created by corresponding factory
class Movie2D(AbstractMovie2D):

    def __init__(self, name, screen, showTimes):
        self.name = name
        self.screen = screen
        self.type = "2D"
        self.subtitled = "Not Subtitled"
        self.showTimes = showTimes

    def get_movie_title(self):
        return self.name

    def get_movie_screen(self):
        return self.screen

    def get_movie_subtitled(self):
        return self.subtitled

    def get_movie_type(self):
        return self.type

    def get_movie_showTimes(self):
        return self.showTimes

    def get_movie_listing(self):       
        output = "Screen " + self.screen
        output += " - " + self.name
        output += " : " + self.subtitled
        output += " - " + self.type
        output += " - Show Times -  "
        for showTime in self.showTimes :
            output += showTime + " "
        return output

class SubtitledMovie2D(AbstractMovie2D):

    def __init__(self, name, screen, showTimes):
        self.name = name
        self.screen = screen
        self.type = "2D"
        self.subtitled = "Subtitled"
        self.showTimes = showTimes

    def get_movie_title(self):
        return self.name

    def get_movie_screen(self):
        return self.screen

    def get_movie_subtitled(self):
        return self.subtitled

    def get_movie_type(self):
        return self.type

    def get_movie_showTimes(self):
        return self.showTimes

    def get_movie_listing(self):       
        output = "Screen " + self.screen
        output += " - " + self.name
        output += " : " + self.subtitled
        output += " - " + self.type
        output += " - Show Times -  "
        for showTime in self.showTimes :
            output += showTime + " "
        return output

# Interface for movie3D product
class AbstractMovie3D(ABC):

    @abstractmethod
    def get_movie_title(self) :
        pass
    @abstractmethod
    def get_movie_screen(self):
        pass
    @abstractmethod
    def get_movie_subtitled(self) :
        pass
    @abstractmethod
    def get_movie_type(self):
        pass
    @abstractmethod
    def get_movie_showTimes(self):
        pass

# products created by corresponding factory
class Movie3D(AbstractMovie3D):
    def __init__(self, name, screen, showTimes):
        self.name = name
        self.screen = screen
        self.type = "3D"
        self.subtitled = "Not Subtitled"
        self.showTimes = showTimes

    def get_movie_title(self):
        return self.name

    def get_movie_screen(self):
        return self.screen

    def get_movie_subtitled(self):
        return self.subtitled

    def get_movie_type(self):
        return self.type

    def get_movie_showTimes(self):
        return self.showTimes

    def get_movie_listing(self):       
        output = "Screen " + self.screen
        output += " - " + self.name
        output += " : " + self.subtitled
        output += " - " + self.type
        output += " - Show Times -  "
        for showTime in self.showTimes :
            output += showTime + " "
        return output

class SubtitledMovie3D(AbstractMovie3D):
    def __init__(self, name, screen, showTimes):
        self.name = name
        self.screen = screen
        self.type = "3D"
        self.subtitled = "Subtitled"
        self.showTimes = showTimes

    def get_movie_title(self):
        return self.name

    def get_movie_screen(self):
        return self.screen

    def get_movie_subtitled(self):
        return self.subtitled

    def get_movie_type(self):
        return self.type

    def get_movie_showTimes(self):
        return self.showTimes

    def get_movie_listing(self):       
        output = "Screen " + self.screen
        output += " - " + self.name
        output += " : " + self.subtitled
        output += " - " + self.type
        output += " - Show Times -  "
        for showTime in self.showTimes :
            output += showTime + " "
        return output