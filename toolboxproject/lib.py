from termcolor import colored


def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    return("Hello, " + name + ". Good morning!")


def who_am_i(name):
    return(colored(f"Hello my name is {name}", "blue"))
