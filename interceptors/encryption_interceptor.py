from utils import utils
from functools import wraps

def encryption_interceptor(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        y = list(args)
        y[1] = utils.encrypt(y[1])
        args = tuple(y)
        result = func(*args, **kwargs)

        return result

    return wrapper