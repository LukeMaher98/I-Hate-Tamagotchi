from bridge import listing_factory


class ConcessionReader:

    def read(self, filename):
        data = open(filename, "r")
        list = []
        for line in data:
            currentline = line.split(",")
            # Remove empty items
            currentline = currentline[:-1]
            list.append(currentline)
        return list


class ConcessionSaleReader:

    def read(self, filename):
        listData = open(filename, "r")
        lineData = listData
        list_data = []
        entryListing = 0
        for line in lineData:
            index = 0
            length = len(line)
            current_entry = ["", "", []]
            while index < length:
                if line[index] == ",":
                    index += 1
                    break
                else:
                    current_entry[0] += line[index]
                index += 1
            while index < length:
                if line[index] == ",":
                    index += 1
                    break
                else:
                    current_entry[1] += line[index]
                index += 1
            list_data.append(current_entry)

        return listing_factory.factory.create_list("concession sale", list_data)


class TicketSaleReader:

    def read(self, filename):
        listData = open(filename, "r")
        lineData = listData
        list_data = []
        entryListing = 0
        for line in lineData:
            index = 0
            length = len(line)
            current_entry = ["", "", []]
            while index < length:
                if line[index] == ",":
                    index += 1
                    break
                else:
                    current_entry[0] += line[index]
                index += 1
            while index < length:
                if line[index] == ",":
                    index += 1
                    break
                else:
                    current_entry[1] += line[index]
                index += 1
            list_data.append(current_entry)

        return listing_factory.factory.create_list("ticket sale", list_data)


class BookingsReader:

    def read(self, filename, user):
        bookings = []
        with open(filename, "r") as db:
            for line in db:
                string = line.split(",")
                if user == string[0]:
                    bookings.append(string[1] + ": " + string[2])

        return bookings


class BookingsReviewReader:

    def read(self, filename):
        dict = {}
        with open(filename, "r") as db:
            for line in db:
                movie = line.split(",")[1]
                if movie not in dict:
                    dict[movie] = 1
                else:
                    dict[movie] = dict[movie] + 1

        dictlist = []
        for key, value in dict.items():
            temp = f"{key}: {value}"
            dictlist.append(temp)

        return dictlist
