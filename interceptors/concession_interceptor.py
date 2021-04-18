from functools import wraps
from controllers import logic_controller

#display multiple orders of a concession on one line instead of a repeating list
def concession_interceptor(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        y = list(args)
        window = y[0]

        #calling addToConcessionsBasket
        func(*args, **kwargs)

        myItems = list(logic_controller.logic.get_concessions_basket()["items"])
        myBasket = []
        countedItems = []

        #couting the number of instances of each item to be displayed
        for i in myItems:
            counter = 0
            if i not in countedItems:
                for j in myItems:
                    if i == j:
                        counter += 1
                myBasket.append(i + ", Amount: " + str(counter))
                countedItems.append(i)

        window['-BASKET-'].update(myBasket)

    return wrapper