# Assertions are fundamental to testing in Python
def add(a, b):
    if a is None or b is None:
        raise ValueError("Both arguements must be provided")
    return a + b

def subtract(a, b):
    return a - b