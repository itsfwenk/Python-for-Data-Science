class calculator:
    """
    A calculator class that is able to do calculations
    of 2 vectors :
        - dot product
        - addition
        - subtraction
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Prints the dot product of the vector passed as parameters.
        """
        dot_product = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {dot_product}")


    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Prints the addition of the vector passed as parameters.
        """
        add_vector = [float(x) + y for x, y in zip(V1, V2)]
        print(f"Add Vector is : {add_vector}")



    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Prints the soustraction of the vector passed as parameters.
        """
        sous_vector = [float(x) - y for x, y in zip(V1, V2)]
        print(f"Sous Vector is : {sous_vector}")
