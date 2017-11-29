def func_injection():
    return "this is confusing"


# Class example
class Example:
    """ This is the Example's docstring
    """
    i = 12345  # class variable shared by all the instances
    fi = func_injection()

    def __init__(self, a=1, b=2):
        self.data = []  # instance variable unique to each instance
        self.a = a
        self.b = b
        self.__update(a, b)

    def update(self, a, b):
        self.a = a
        self.b = b

    __update = update  # private copy of original update() method

    def f(self):
        return 'hello world'

    def get_docstring(self):
        return self.__doc__

    def add_data(self, data=None):
        if data:
            self.data.append(data)

    def get_data(self):
        return self.data

    def add_data_twice(self, data=None):
        self.add_data(data)
        self.add_data(data)


# Sub class
class SubExample(Example):
    def update(self, c):
        # provides new signature for update()
        # but does not break __init__()
        self.a = c


# Car
class Car:
    pass


# Multiple inheritance
class DoubleExample(SubExample, Car):
    pass


# Exception class
class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")


# Iterator
class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


rev = Reverse('spam')
iter(rev)
for char in rev:
    print(char)


# Generator
def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


for char in reverse('golf'):
    print(char)

# creates empty DoubleExample record
de = DoubleExample()
de.name = "Sample 1"
de.direction = "South"
de.update("T1")
print(de.a)

# create class object
x = Example(5, 10)
print(x.get_docstring())
print(x.b)

# instance objects
x.counter = 1
while x.counter < 10:
    x.counter *= 2
print(x.counter)
del x.counter

# store method for later consumption
xf = x.f
for i in range(5):
    print(xf())

# working with dictionaries
x.add_data("a")
x.add_data("b")
print(x.get_data())

# function injection - confusing
print(x.fi)


# variables scope
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        # nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
