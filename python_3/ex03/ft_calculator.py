class calculator:
    """
    A calculator class that is able to do calculations
    of vector with a scalar :
        - addition
        - multiplication
        - subtraction
        - division
    It overloads the +, -, *, and / operators for vector-scalar calculations.
    """

    def __init__(self, vector):
        """
        Vector constructor.

        Args:
            vector (list): List to be put in the vector.
        """
        self.vector = vector


    def __add__(self, object) -> None:
        """
        Addition method. Prints the resulting vector.
        """
        self.vector = [x + object for x in self.vector]
        print(self.vector)
        # return [x for x in self.vector]

    def __mul__(self, object) -> None:
        """
        Multiplication method. Prints the resulting vector.
        """
        self.vector = [x * object for x in self.vector]
        print(self.vector)


    def __sub__(self, object) -> None:
        """
        Subtraction method. Prints the resulting vector.
        """
        self.vector = [x - object for x in self.vector]
        print(self.vector)


    def __truediv__(self, object) -> None:
        """
        Division method. Prints the resulting vector.
        """
        try:
            if object == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            self.vector = [x / object for x in self.vector]
            print(self.vector)
        except ZeroDivisionError as error:
            print(ZeroDivisionError.__name__ + ":", error)