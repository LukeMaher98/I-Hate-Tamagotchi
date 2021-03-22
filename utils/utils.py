from entities import listings
from entities import list_objects
import re

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
    f = open(filename, "w")
    for l in list:
        f.write(l)
    f.close()


def convertToEditForm(input):
    o = input.split(' -')[0]
    input = input.replace(o+" -  ", "")
    o = o.replace("Screen ", "")
    output = input.split(': ')[0]
    t = input.replace(output+":  ", "")
    output = output + "," + o + ","
    output = output + t.replace(" ", ",")
    output = output.removesuffix(",")

    return output

def convertToSaveForm(input):
    o = input.split(' -')[0]
    input = input.replace(o+" -  ", "")
    o = o.replace("Screen ", "")
    output = input.split(': ')[0]
    t = input.replace(output+": ", "")
    output = output + "," + o
    output = output + t.replace(" ", ", ")

    return output

def convertToDisplayForm(input):
    elements = input.split(",")
    count = 0
    output = ""
    t = ""
    for element in elements:
        if count == 0 : 
            t = element + ":  "
        elif count == 1:
            if re.match("[0-9][0-9]|[0-9]", element):
                output = "Screen " + element + " -  " + t
        else:
            if re.match("(2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9])", element):
                output += element + " "
        count += 1

    return output

def deleteSelected(delete, values):
    output = []
    for v in values:
        if v != delete:
            output.append(v)

    return output   