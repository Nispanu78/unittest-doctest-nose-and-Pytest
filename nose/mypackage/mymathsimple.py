class mymathsimple():
    def __init__(self):
        print("Creating object : " + self.__class__.__name__)

    def add(x, y):
        return(x + y)

    def mul(x, y):
        return(x * y)

    def sub(x, y):
        return(x - y)

    def div(x, y):
        return(x / y)

    def __del__(self):
        """Destructor for this class..."""
        print("Destroying object : " + self.__class__.__name__ )
