# coding=utf-8

class Car:
    __isinstance=None
    def __init__(self):
        pass
    def __new__(cls, *args, **kwargs):
        if cls.__isinstance==None:
            cls.__isinstance=object.__new__(cls,*args)
        return cls.__isinstance



a=Car()
b=Car()
print(id(a),id(b))

