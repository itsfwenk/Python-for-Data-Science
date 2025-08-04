from S1E9 import Character


class Baratheon(Character):
    """
    A concrete class representing a character from the
    Baratheon family, inheriting from Character.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initialize a Baratheon character with the provided first name.

        Parameters:
            first_name (str): The first name of the character.
            super: calling the __init__ method of the parent class Character
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """
        An abstract method to get the string representation of the object.
        """
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        """
        An abstract method to get a strings representation of the object.
        """
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"


class Lannister(Character):
    """
    A concrete class representing a character from the
    Lannister family, inheriting from Character.
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initialize a Lannister character with the provided first name.

        Parameters:
            first_name (str): The first name of the character.
            super: calling the __init__ method of the parent class Character
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """
        An abstract method to get the string representation of the object.
        """
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        """
        An abstract method to get a strings representation of the object.
        """
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """
        A class method to create and return a new Lannister character.

        Args:
            first_name (str): The first name of the new Lannister character.
            is_alive (bool, optional): Health state, True by default.

        Returns:
            A Lannister character.
        """
        return cls(first_name, is_alive)
