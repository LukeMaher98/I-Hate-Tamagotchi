from entities import listings
from entities import list_objects
import re
from entities import abstract_factory

def read_file(filename):
    data = open(filename, "r")
    list = []
    for line in data: 
        currentline = line.split(",")
        # Remove empty items
        currentline = currentline[:-1]
        list.append(currentline)
    return list

def get_view_list(type, filename):
        listData = open(filename, "r")
        lineData = listData
        list_data = []
        entryListing = 0
        for line in lineData:
            index = 0
            length = len(line)
            current_entry = ["","",[]]
            while index < length:
                if line[index] == ",":
                    index += 1
                    break
                else:
                    current_entry[0] +=line[index]
                index += 1
            while index < length:
                if line[index] == ",":
                    index += 1
                    break
                else:
                    current_entry[1] +=line[index]
                index += 1
            hold = ""
            if type == "movies" :
                while index < length:
                    if line[index] == ",":
                        index += 1
                        current_entry[2].append(hold)
                        hold = ""
                    else:
                        hold +=line[index]
                    index += 1
                hold = hold[:-1]
                current_entry[2].append(hold)
                entryListing = list_objects.Movie(current_entry)
            if type == "concessions":
                entryListing = list_objects.Concession(current_entry)
            if type == "concession sale":
                entryListing = list_objects.ConcessionSales(current_entry)
            if type == "ticket sale":
                entryListing = list_objects.TicketSales(current_entry)
            list_data.append(entryListing)
        
        return list_data

def save_to_file(filename, content):
    f = open(filename, "w")  
    for c in content:
        n = c.split(': ')[0]
        t = c.replace(n+":", "")
        n = n + "," + t.replace("  ", "")
        if n.endswith("\n") != True:
            n = n + "\n"
        f.write(n)

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

def read_bookings(user):
    bookings = []
    with open("databases/bookings_db.txt", "r") as db:
        for line in db:
            string = line.split(",")
            if user == string[0]:
                bookings.append(string[1] + ": " + string[2])
    
    return bookings

def read_bookings_review():
    dict = {}
    bookings = []
    with open("databases/bookings_db.txt", "r") as db:
        for line in db:
            movie = line.split(",")[1]
            if movie not in dict:
                dict[movie] = 1
            else:
                dict[movie] = dict[movie] + 1
    
    return dict.items()

def get_list(filename):
    f = open(filename, "r")
    lines = f.readlines()  

    return lines  

def save_list(filename, list):
    f = open("screenings_db.txt", "a")
    print(list)
    f.write(list+'\n')
    f.close()


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
    print(element)
    if(element != ""):
        with open(filename, 'a') as file:
            file.write(element+"\n")

def write_to_file(filename, element):
    with open(filename, 'w') as file:
        file.write(element+"\n")

def verify_format(input):
    elements = input.split(",")
    count = 0
    output = ""
    t = ""
    #r = re.compile('.{12},.{3},.{2},.{13}')
    for element in elements:
        count += 1
     #if count == 0:
         #   if re.match("[0-9][0-9]|[0-9]", element):
          #      print("NAME MATCHES")
        #elif count == 1:
         #   if re.match("[0-9][0-9]", element):
          #      print("SCREEN MATCHES")
        #elif count == 2:
         #   if re.match("[0-9][0-9]", element):
          #      print("Type MATCHES")
        #elif count == 3:
         #   if re.match("[0-9][0-9]", element):
          #      print("SUBTITLED MATCHES")
    if count >= 5:
        return True
    else:
        return False

def get_movie_format():
    file = open('databases/screenings_db.txt', 'r')
    screenings_info = file.readlines()  
    screenings_list = get_movie_objetcs(screenings_info)

    movie_list_output = []
    for movie in screenings_list:
        output = ""
        output += "Screen " +movie.get_movie_screen()
        output += " - "+movie.get_movie_title()
        output += " : "+movie.get_movie_subtitled()
        output += " - "+movie.get_movie_type()
        output += " - Show Times -  "
        for showTime in movie.get_movie_showTimes() :
            output += showTime+" "
        movie_list_output.append(output)

    return movie_list_output


def get_movie_objetcs(screenings_info):
    screenings_list = []
    factoryStandard = abstract_factory.MovieStandard()
    factorySubtitled = abstract_factory.MovieSubtitled()

    for line in screenings_info:
        movie_info = line.split(',')
        show_times = []
        output = ""
        i = 4
        while i < len(movie_info)-1:
            output += " "+ movie_info[i]
            i += 1
        show_times.append(output)

        if(movie_info[2] == "2D"):
            if(movie_info[3] == "Subtitled"):
                movie = factorySubtitled.create_2D_movie(movie_info[0], movie_info[1], show_times)
            else:
                movie = factoryStandard.create_2D_movie(movie_info[0], movie_info[1], show_times)
        if(movie_info[2] == "3D"):
            if(movie_info[3] == "Subtitled"):
                movie = factorySubtitled.create_3D_movie(movie_info[0], movie_info[1], show_times)
            else:
                movie = factoryStandard.create_3D_movie(movie_info[0], movie_info[1], show_times)
        screenings_list.append(movie)
 
    return screenings_list 

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
