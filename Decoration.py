# -*- coding: utf-8 -*-

def outer(func):
    def inner():
        print('call %s():', func.__name__)
        return func()
    return inner

def foo():
    pass
    
decorated = outer(foo)
decorated()
print(decorated.__name__)
