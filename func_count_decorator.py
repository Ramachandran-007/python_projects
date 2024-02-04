def fun_count(func):
    def inner (*args,**kwargs):

        func(*args,**kwargs)

    return inner

@fun_count
def add(a,b):
    return a+b

@fun_count
def sub(a,b):
    return a-b

@fun_count
def mul(a,b):
    return a*b
