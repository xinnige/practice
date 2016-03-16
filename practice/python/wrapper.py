from functools import wraps

def func_wrapper(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        print "params is ", args[1:], kwargs, 
        r = func(*args, **kwargs)
        print ", return value is ", r, 
        print ", params becomes ", args[1:], kwargs 
        return r
    return wrapped
