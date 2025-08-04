from abc import ABC, abstractmethod


class Character(ABC):
    """
    An abstract class "character".

    Attributes:
        first_name (str): The first name of the character.
        is_alive (bool): The health state of the character
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Character constructor.

        Args:
            first_name (str) : First name
            is_alive (bool, optional): Health state, True by default
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        Concrete method that changes is_alive from True to False.
        """
        if self.is_alive:
            self.is_alive = False
            # print(f"{self.first_name} is dead.")
        else:
            # print(f"{self.first_name} is already dead.")
            pass

    @abstractmethod
    def __str__(self):
        """
        An abstract method to get the string representation of the object.
        """
        # return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"
        pass

    @abstractmethod
    def __repr__(self):
        """
        An abstract method to get a strings representation.
        """
        pass
        # return self.__str__()


class Stark(Character):
    """
    A concrete class representing a character from the Stark family,
    inheriting from Character.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Constructor for a new Stark instance.

        Args:
            first_name (str): The first name of the Stark character.
            is_alive (bool, optional): Health state, True by default
        """
        super().__init__(first_name, is_alive)
        # print(f"Stark character '{self.first_name}' created.")
