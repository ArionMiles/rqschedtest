import random

def say_hello(name=None):
    """A job with a single argument and a return value."""
    rid = random.randrange(0, 1000)
    if name is None:
        name = 'Stranger'
    return 'Hi there, %s - %s!' % (name, rid)
