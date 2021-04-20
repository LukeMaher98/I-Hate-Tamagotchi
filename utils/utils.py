from bridge import listing_factory
from facade import facade
from utils import utils

reader = facade.Reader()

# true for ui format, false for database format
def title_times_split(string, ui):
    title = string[:string.index(":")]
    showTimes = []

    string = string[string.index(":")+1:]
    if ui:
        while True:
            if ":" in string:
                showTimes.append(title + ": " + string[string.index(":")-2:string.index(":")+3])
                string = string[string.index(":")+1:]
            else:
                break
    else: 
        while True:
            if ":" in string:
                showTimes.append(string[string.index(":")-2:string.index(":")+3])
                string = string[string.index(":")+1:]
            else:
                break

    return title, showTimes

def deleteSelected(delete, values, filename):
    count = 0
    index = 0
    for value in values :
        if value == delete:
            index = count +1 
        else:
            count += 1

    with open(filename, "r") as f:
        lines = f.readlines()

    count = 0
    with open(filename, "w") as f:
        for line in lines:
            count += 1
            if count != index:
             f.write(line) 

def append_to_file(filename, element):
    if(element != ""):
        with open(filename, 'a') as file:
            file.write(element+"\n")

def write_to_file(filename, element):
    with open(filename, 'w') as file:
        file.write(element+"\n")

def verify_format(input):
    elements = input.split(",")
    if len(elements) >= 5:
        return True
    else:
        return False

def getMovieListings():
    movie_info = reader.read("databases/screenings_db.txt", "ticket")
    movie_list = listing_factory.factory.create_list(
        "movie", movie_info)
    return movie_list.generate_list()

plainArr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
encrArr = ["x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
            "9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]

def encrypt(password):

    newpassword = ""
    for element in password:
        try:
            i = plainArr.index(element)
        except:
            newpassword += element
        else:
            newpassword += encrArr[i]

    return newpassword 

def decrypt(password):

    newpassword = ""
    for element in password:
        try:
            i = encrArr.index(element)
        except:
            newpassword += element
        else:
            newpassword += plainArr[i]

    return newpassword 
