from functools import wraps
from controllers import logic_controller

#display multiple orders of a concession on one line instead of a repeating list
def concession_interceptor(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        y = list(args)
        window = y[0]

        #calling addToConcessionsBasket
        result = func(*args, **kwargs)

        myItems = list(logic_controller.logic.get_concessions_basket()["items"])
        myBasket = []

        #couting the number of instances of each item to be displayed
        for i in myItems:
            counter = 0
            for j in myItems:
                if i == j:
                    counter += 1
            myBasket.append(i + ", Amount: " + str(counter))
            myItems[:] = (k for k in myItems if k != i)

        window['-BASKET-'].update(myBasket)

    return wrapper