from utils import utils
from functools import wraps

#encrypt the new user passwords before saving them to the db
def encryption_interceptor(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        y = list(args)

        #encrypting the password
        y[1] = utils.encrypt(y[1])
        args = tuple(y)

        #calling save_new_user_data with the encrypted password
        result = func(*args, **kwargs)

        return result

    return wrapper