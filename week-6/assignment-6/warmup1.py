#Default parameters
def greet(name, greeting="Ahoy there"):
    '''
    Prints a greeting.
    
    :param name: Name argument
    :param greeting: Custom greeting message 
    '''
    print(f"{greeting},{name}!")

greet("Sasha")
greet("Sasha","Good morning")
greet("Sasha", greeting="Good evening")