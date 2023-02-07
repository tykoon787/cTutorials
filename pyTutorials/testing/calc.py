def add(x, y):
    """ Add Function """
    return x + y

def subtraction(x, y):
    """Subtraction Function"""
    return x - y

def multiply(x, y):
    """Product Function"""
    return x * y

def divide(x , y):
    """Divide Function"""
    if y == 0:
        raise ValueError("Can't Divide by Zero!")
    return x / y
