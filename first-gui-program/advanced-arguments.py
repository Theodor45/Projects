def my_function(a, b, c):
    # Do this with a
    # Do that with b
    # Then do this with c
    pass

def another_function(a = 1, b = 2, c = 3, d = None):
    # You can leave default arguments to a function like this
    # If you don't want an error when you run a function without a unnecessery argument
    # Then you can just use None as the default argument
    pass

# In previous projects, we used functions to sum, multiply, divide, etc.
def add(a, b):
    return a + b
# But here, if i want to add more numbers i have to add more arguments in the function

# Instead, you can use *args to get infinite arguments if needed
def add(*args):
    print(type(args))
    total = 0
    for f in args:
        total += f
    return total
# As you can see, all the given arguments are stored like a tuple
# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))


# **kwargs is exactly like *args but the arguments are stored in a dictionary,
# So you can use the args by their names and not only by their position that they were given in
def calculate(**kwargs):
    total = 0
    print(type(kwargs))
    for f in kwargs:
        if f == 'divide':
            print("There was a key word argument with 'divide'.")


class Car:

    def __init__(self, **kw):
        self.model = kw.get('model')
        self.make = kw.get('make')

    def print_da_thing(self):
        print(self.make)
        print(self.model)

honda = Car(make='Nissan', model='skyline r34')
honda.print_da_thing()