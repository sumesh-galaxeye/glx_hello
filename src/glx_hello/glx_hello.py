'''
This is how we greet people at Galaxeye
'''

def say_hello(name=None):
    if name is None:
        return "Hey, what's your good name? Anyways lets propel together!"
    else:
        return f"Hello, {name}!, lets propel together!"