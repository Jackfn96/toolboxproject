def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    return("Hello, " + name + ". Good morning!")

if __name__ == "__main__":
    res = greet('Jack')
    print(res)