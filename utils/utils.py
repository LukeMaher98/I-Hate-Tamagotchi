from abstract_factory import abstract_factory

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
    count = 0
    output = ""
    t = ""
    for element in elements:
        count += 1
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
